class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[0 for i in range(n)] for j in range(m)]
        topRow=0
        bottomRow=m-1
        leftCol=0
        rightCol=n-1
        curr=head
      
        while(leftCol<rightCol+1 and topRow<bottomRow+1):
            #topRow
            for j in range(leftCol,rightCol+1):
                if curr:
                    matrix[topRow][j]=curr.val
                    curr=curr.next
                else:
                    matrix[topRow][j]=-1
            topRow+=1
          
            #RightCol
            for i in range(topRow,bottomRow+1):
                if curr:
                    matrix[i][rightCol]=curr.val
                    curr=curr.next
                else:
                    matrix[i][rightCol]=-1
            rightCol-=1
            
            #bottomRow
            if topRow<bottomRow:
                for j in range(rightCol,leftCol-1,-1):
                    if curr:
                        matrix[bottomRow][j]=curr.val
                        curr=curr.next
                    else:
                        matrix[bottomRow][j]=-1
                bottomRow-=1
                
            #leftCol    
            if leftCol<rightCol:
                for i in range(bottomRow,topRow-1,-1):
                    if curr:
                        matrix[i][leftCol]=curr.val
                        curr=curr.next
                    else:
                        matrix[i][leftCol]=-1
                leftCol+=1
            
        return matrix
