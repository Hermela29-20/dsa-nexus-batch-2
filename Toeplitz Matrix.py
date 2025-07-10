class Solution(object):
      def isToeplitzMatrix(self, matrix) :
          a=len(matrix) 
          b=len(matrix[0])
          for i in range(a-1):
            for j in range(b-1):
                if matrix[i][j]==matrix[i+1][j+1]:
                    return True
          return False

        
