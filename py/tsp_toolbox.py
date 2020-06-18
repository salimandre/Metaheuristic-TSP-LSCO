'''
tools to solve TSP instances: dj38 and 
'''
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
import json

class TSP:
	def __init__(self, path_data):

		# load json file
		name_tsp=path_data.split('/')[-1]
		with open(path_data+'/'+name_tsp+'.json') as json_file:
		    self.json_tsp=json.load(json_file)

		# init n_cities
		self.n_cities=int(self.json_tsp['n_cities'])

		# load cities coord
		tsp_coord=np.zeros((self.json_tsp['n_cities'],2))
		f = open(path_data+'/'+self.json_tsp['coord'], "r")
		for i, line in enumerate(f.readlines()):
			str_coord=line.strip().split(' ')[1:]
			y=float(str_coord[0])
			x=float(str_coord[1])
			coord=(x,y)
			tsp_coord[i,:]=coord

		minX=np.min(tsp_coord[:,0])
		maxX=np.max(tsp_coord[:,0])
		minY=np.min(tsp_coord[:,1])
		maxY=np.max(tsp_coord[:,1])

		tsp_coord[:,0]= (tsp_coord[:,0]-minX)*self.json_tsp['img_dim'][0]/(maxX-minX)
		tsp_coord[:,1]= (tsp_coord[:,1]-minY)*self.json_tsp['img_dim'][1]/(maxY-minY)
		
		self.map=tsp_coord

		# init map path
		self.path=list(range(self.n_cities))+[0]

		# loads img_bg
		self.img_bg = plt.imread(path_data+'/'+self.json_tsp['img'])

		# keep the way to scale coord back
		self.scale_back_X = lambda x: (maxX-minX)*x/self.json_tsp['img_dim'][0] + minX
		self.scale_back_Y = lambda y: (maxY-minY)*y/self.json_tsp['img_dim'][1] + minY

	@property
	def X(self):
	    return self.map[:,0]
	@X.setter
	def X(self, mapX):
		self.map[:,0]=mapX

	@property
	def Y(self):
	    return self.map[:,1]
	@Y.setter
	def Y(self, mapY):
		self.map[:,1]=mapY

	@property
	def path(self):
	    return self._path

	@path.setter
	def path(self, list_ind):
		self._path=list_ind+[list_ind[0]]

	@property
	def cost(self):
	    return np.sqrt(np.sum((self.map[self.path[:-1]] - self.map[self.path[1:]])**2, axis=1)).sum()

	@property
	def edges(self):
	    return [set(edge) for edge in zip(self.path[:-1], self.path[1:])]

	def show_cities(self, display_time):
		# display background
		fig, ax = plt.subplots() #figsize=(6, 9)
		ax.imshow(self.img_bg, extent=self.json_tsp["extent_axes_window"])#[-75,429,-70,460])
		ax.axis('off')
		# display vertices
		plt.scatter(self.X[self.path[:-1]], self.Y[self.path[:-1]], c='red', zorder=2)
		for i in range(len(self.path)-1):
			plt.text(self.X[self.path[:-1]][i]+10, self.Y[self.path[:-1]][i]+10,s=str(self.path[i]), fontdict={'color': 'red', 'fontsize': 9})

		plt.show(block=False)
		plt.pause(display_time)
		plt.close()

	def show(self, display_time, show_cost=False):
		# display background
		fig, ax = plt.subplots() #figsize=(6, 9)
		ax.imshow(self.img_bg, extent=self.json_tsp["extent_axes_window"])
		ax.axis('off')
		# display edges
		plt.plot(self.X[self.path], self.Y[self.path], lw=3, zorder=1)
		# display vertices
		plt.scatter(self.X[self.path[:-1]], self.Y[self.path[:-1]], c='red', zorder=2)
		plt.scatter(self.X[self.path[-1]], self.Y[self.path[-1]], c='lime', zorder=2)
		# display cost
		if show_cost:
			plt.text(-50, 350, s='cost: '+str(round(self.cost,1)), fontdict={'color': 'purple', 'fontsize': 12, 'backgroundcolor': 'white'})
		# display figure
		plt.title(self.json_tsp["name"])
		#plt.gcf().show()#block=False)
		plt.show(block=False)
		plt.pause(display_time)
		plt.close()

	def random_path(self, len_path):
		rand_path=random.sample(list(range(self.n_cities)), len_path)
		random.shuffle(rand_path)
		self.path=rand_path

	def __find_new_edge_with_greed(self,ind_city):
		best_cost=1e10
		for j in range(self.n_cities):
				if j not in self.path:
					cost_ij=np.sqrt( ((self.map[j] - self.map[ind_city])**2).sum() )
					if cost_ij<best_cost:
						best_cost=cost_ij
						best_edge=(ind_city,j)
		return best_edge[1]

	def __find_shortest_edge(self):
		best_cost=1e10
		for i in range(self.n_cities):
			for j in range(self.n_cities):
				if i>j:
					cost_ij=np.sqrt( ((self.map[i] - self.map[j])**2).sum() )
					if cost_ij<best_cost:
						best_cost=cost_ij
						best_edge=(i,j)
		return best_edge

	def greedy_solver(self, display_time=0, show_cost=False):

		tic=time.time()
		cost_history=[]

		best_edge=self.__find_shortest_edge()
		self.path=[best_edge[0],best_edge[1]]
		cost_history+=[self.cost]

		if display_time>0:
			self.show(display_time=display_time, show_cost=show_cost)

		for i in range(self.n_cities-2):
			new_city = self.__find_new_edge_with_greed(self.path[-1])
			self.path.pop()
			self.path=[new_city]+self.path
			cost_history+=[self.cost]

			if display_time>0:
				self.show(display_time=display_time, show_cost=show_cost)

		toc=time.time()

		'''
		plt.plot(np.arange(2,self.n_cities+1,1), cost_history, label='cost')

		
		p = np.polyfit(np.arange(2,self.n_cities+1,1), cost_history,deg=1)
		plt.plot(np.arange(2,self.n_cities+1,1), p[0]*np.arange(2,self.n_cities+1,1)+p[1],'r--', label=str(round(p[0],1))+'n_cities'+str(round(p[1],1)))

		plt.xticks(list(range(2,self.n_cities+1,2)))
		plt.xlabel('nb of cities')
		plt.ylabel('distance')
		plt.title('greedy algo: cost vs n_cities')
		plt.legend(loc='upper left')
		plt.show()
		'''
		print('*\nsolution by greedy policy in ',round(toc-tic,3),'s: ',cost_history[-1],'\n*\n')

	def scale_back(self):
		self.X=self.scale_back_X(self.X)
		self.Y=self.scale_back_Y(self.Y)

	def __compute_distance_matrix(self):
		dist_mat=np.zeros((self.n_cities,self.n_cities))
		for i in range(self.n_cities):
			for j in range(i+1,self.n_cities):
				dist_mat[i,j]=np.sqrt(np.sum((self.map[i] - self.map[j])**2) )
				dist_mat[j,i]=float(dist_mat[i,j])
		return dist_mat

	def swap(self,el_1,el_2):
		# swap el_1 el_1 in list self.path
		pos_1=self.path.index(el_1)
		pos_2=self.path.index(el_2)

		pos_1, pos_2=sorted([pos_1,pos_2])
		el_1=self.path[pos_1]
		el_2=self.path[pos_2]

		self.path.pop(pos_1)
		self.path.insert(pos_2-1, el_1)

		self.path.pop(pos_2)
		self.path.insert(pos_1, el_2)

		# update path (in case root has been swaped)
		self.path=self.path[:-1]

	# implement 5 non trivial 3-perm with 2-perm
	def __random_tri_swap(self, i, trio):
		if i==1:
			self.swap(trio[1],trio[2])
		if i==2:
			self.swap(trio[0],trio[1])
		if i==3:
			self.swap(trio[0],trio[2])
		if i==4:
			self.swap(trio[0],trio[1])
			self.swap(trio[0],trio[2])
		if i==5:
			self.swap(trio[0],trio[2])
			self.swap(trio[0],trio[1])

	def k_swap_solver(self, n_iters, display_time=0, show_cost=False, init_with='random', k=2):
		if not (k==2 or k==3):
			print('*** warning ***\nk = ',k,' has not been implemented yet! Sorry :(\n')
			return 0	
		tic=time.time()

		cost_history=[]

		if init_with=='random':
			self.random_path(self.n_cities)
		if init_with=='greedy':
			self.greedy_solver(display_time=display_time, show_cost=show_cost)

		cost_history+=[self.cost]
		best_cost=cost_history[0]

		if k==2:
			couples=[(i,j) for i in range(self.n_cities) for j in range(i+1,self.n_cities)]
		if k==3:
			couples=[(i_perm, i,j,k) for i_perm in range(1,math.factorial(k)) for i in range(self.n_cities) for j in range(i+1,self.n_cities) for k in range(j+1,self.n_cities)]
		random.shuffle(couples)
		iter_couples=iter(couples)

		cnt_iters=0
		cnt_swaps=0
		cnt_local_min=0
		try:
			while cnt_iters<n_iters:

				no_swap=list(self.path)

				next_couple=next(iter_couples)
				if k==2:
					self.swap(next_couple[0],next_couple[1])
				if k==3:
					self.__random_tri_swap(next_couple[0],next_couple[1:])

				new_cost=self.cost
				if new_cost<best_cost:
					cnt_swaps+=1
					cnt_local_min=0
					best_cost=new_cost

					if display_time>0:
						self.show(display_time=display_time,show_cost=show_cost)
					print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',best_cost)

					if k==2:
						couples=[(i,j) for i in range(self.n_cities) for j in range(i+1,self.n_cities)]
					if k==3:
						couples=[(i_perm, i,j,k) for i_perm in range(1,math.factorial(k)) for i in range(self.n_cities) for j in range(i+1,self.n_cities) for k in range(j+1,self.n_cities)]
					
					random.shuffle(couples)
					iter_couples=iter(couples)
				else:
					self.path=no_swap[:-1]
				cnt_iters+=1
				cnt_local_min+=1
				cost_history+=[best_cost]

			toc=time.time()
			print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',best_cost)
			print('*\nsolution by ',k,'swap in ',round(toc-tic,1),'s: ',cost_history[-1],'\n*\n')

			plt.plot(list(range(1,len(cost_history)+1)), cost_history)
			plt.xlabel('n_iters')
			plt.ylabel('distance')
			plt.title(str(k)+'-swaps init '+init_with+' algo: distance vs n_iters')
			plt.show()

		except StopIteration:
			toc=time.time()
			print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',best_cost)
			print('*\nsolution by ',k,'swap in ',round(toc-tic,1),'s: ',cost_history[-1],'\n*\n')

			plt.plot(list(range(1,len(cost_history)+1)), cost_history)
			plt.xlabel('n_iters')
			plt.ylabel('distance')
			plt.title(str(k)+'-swaps init '+init_with+' algo: distance vs n_iters')
			plt.show()


	def k_opt_solver(self, n_iters=1, display_time=0, show_cost=False, init_with='random', k=2):

		if k!=2:
			print('*** warning ***\nk = ',k,' has not been implemented yet! Sorry :(\n')
			return 0	

		tic=time.time()

		# store distance matrix
		dist_mat = self.__compute_distance_matrix()

		# initialization
		if init_with=='random':
			self.random_path(self.n_cities)
		if init_with=='greedy':
			self.greedy_solver(display_time=display_time, show_cost=show_cost)

		cost_history=[self.cost]

		edges=self.edges
		availabe_edges=[{a,b} for a in range(self.n_cities) for b in range(a+2,self.n_cities)]
		availabe_edges.remove({0,self.n_cities-1})
		random.shuffle(availabe_edges)
		iter_edges=iter(availabe_edges)

		cnt_iters=0
		cnt_swaps=0
		try:
			while cnt_iters<n_iters:

				i_,j_=next(iter_edges)
				e_i, e_j=edges[i_], edges[j_]

				tail=self.path[-2:]	
				if (set(tail)==e_i or set(tail)==e_j):
					pos=[pos_+1 for pos_, v in enumerate(self.path[1:]) if v in e_i.union(e_j)]
				else:
					pos=[pos_ for pos_, v in enumerate(self.path[:-1]) if v in e_i.union(e_j)]

				pos_1, pos_2, pos_3, pos_4=pos
				v_1, v_2, v_3, v_4=self.path[pos_1], self.path[pos_2], self.path[pos_3], self.path[pos_4]

				old_cost=dist_mat[v_1,v_2]+dist_mat[v_3,v_4]
				new_cost=dist_mat[v_1,v_3]+dist_mat[v_2,v_4]

				if new_cost<old_cost:
					cost_history+=[cost_history[-1]+new_cost-old_cost]
					# perform k-opt step
					self.path=self.path[:pos_1+1]+self.path[pos_2:pos_3+1][::-1]+self.path[pos_4:-1]
					cnt_swaps+=1
					print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',cost_history[-1])
					if display_time>0:
						self.show(display_time=display_time,show_cost=show_cost)

					# update neighboorhood graph
					edges=self.edges
					availabe_edges=[{a,b} for a in range(self.n_cities) for b in range(a+2,self.n_cities)]
					availabe_edges.remove({0,self.n_cities-1})
					random.shuffle(availabe_edges)
					iter_edges=iter(availabe_edges)
				else:
					cost_history+=[cost_history[-1]]
					availabe_edges.remove({i_,j_})

				cnt_iters+=1

			toc=time.time()
			print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',cost_history[-1])
			print('*\nsolution by ',k,'-opt in ',round(toc-tic,1),'s: ',cost_history[-1],'\n*\n')

			plt.plot(list(range(1,len(cost_history)+1)), cost_history)
			plt.xlabel('n_iters')
			plt.ylabel('distance')
			plt.title('2-opt algo: distance vs n_iters')
			plt.show()

		except StopIteration:
			toc=time.time()
			print('cost after '+str(cnt_iters+1)+' iters | '+str(cnt_swaps)+' swaps : ',cost_history[-1])
			print('*\nsolution by ',k,'-opt in ',round(toc-tic,1),'s: ',cost_history[-1],'\n*\n')
			
			plt.plot(list(range(1,len(cost_history)+1)), cost_history)
			plt.xlabel('n_iters')
			plt.ylabel('distance')
			plt.title('2-opt algo init '+init_with+' : distance vs n_iters')
			plt.show()
			






