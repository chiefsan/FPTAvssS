import itertools
import collections
import numpy as np

class Solver:

    '''
    Solver class.
    '''

    def __init__(self, Y, M, epsilon, distance):
        '''
        Parameters
        ----------
            Y : list<vector>
                Finite set of vectors
            M : int
                Positive integer lesser than the size of Y
            epsilon : float
                Relative error
            distance : callable
                Distance metric
        '''
        self.Y = Y
        if isinstance(Y[0], int):
            self.q = 1
        else:
            self.q = len(Y[0])
        self.M = M
        self.epsilon = epsilon
        self.distance = distance

    def solve(self):        
        min_obj_fun_val = 1e10
        opt_subset = []
        for y in self.Y:
            ZMyY = self.computeZMvY(y) # M elements of Y closest to y

            rMyY = ZMyY[-1][-1] # maximal distance between y and elements in ZMyY
            
            h = self.epsilon*1.0 / (self.q*self.M)**0.5 * rMyY

            H = self.M**0.5 * rMyY

            if rMyY==0:
                return ZMyY

            ByhH = self.generateByhH(y,h,H)
            
            for b in ByhH:
                
                ZMbY = self.computeZMvY(b)

                subset = [i[0] for i in ZMbY]

                obj_fun_val = self.computeObj(subset)

                if obj_fun_val < min_obj_fun_val:
                    min_obj_fun_val = obj_fun_val
                    opt_subset = subset
        
        return opt_subset, min_obj_fun_val

    def generateByhH(self, y, h, H):
        if self.q==1:
            return np.hstack((
                np.arange(y, -1*H, h), np.arange(y, H, h)
            ))
        arr = [[] for i in range(self.q)]
        for i in  range(self.q):
            arr[i] = np.hstack((
                np.arange(y[i], -1*H, -1*h), np.arange(y[i], H, h)
            ))
        out = []
        n = self.q
        indices = [0 for i in range(n)]
        while (1):
            out.append([])
            for i in range(n):
                out[-1].append(arr[i][indices[i]])
            next = n - 1
            while (next >= 0 and
                (indices[next] + 1 >= len(arr[next]))):
                next-=1
            if (next < 0):
                return out
            indices[next] += 1
            for i in range(next + 1, n):
                indices[i] = 0
        return out

    def computeObj(self, Y):
        Y = np.array(Y)

        y_mean = sum(Y)/len(Y)

        val = 0

        for y in Y:
            val += self.distance(y, y_mean)

        return val


        
    def computeZMvY(self, y):
        dist = collections.OrderedDict()
        for v in self.Y:
            dist[v] = self.distance(y, v)
        dist = sorted(dist.items(), key=lambda kv: kv[1])
        return dist[:self.M]
        
    


