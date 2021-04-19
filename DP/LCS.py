#
# def lcs_length(x ,y): m=len( x)
#     n=len ( y)
#     c=[[0 for i in range(n+1)] fo r j in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if x[i-1]==y [ j- 1] :
#                 c[i][j]=c[i-1 ] [j- 1 ]+1
#             else:
#                 c[i][j]=max(c [ i-1][j] , c[i][j -1])
#     return c[m][n]
#
# def \
#
#
# lcs(x,y):
#     m=len( x )
#     n=len( y )
#     c=[[0 fo r i in range(n+1)] f o r j in range(m+1)]
#     b=[[0 f o r i in range(n+1)] f o r j in range(m+1)]#  1  zu  oshang 2 up 3 left
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if x[i-1]==y [ j- 1] :
#                 c[i][j]=c[i-1 ] [j- 1 ]+1
#                 b[i][j]=1
#             else:
#                 if c[i-1][j] > =c[i] [j -1]:
#                     b[i][j]=2
#                     c[i][j]=c[i-1 ] [j]
#                 else:
#                     b[i][j]=3
#                     c[i][j]=c[i][ j -1]
#     return c[m][n],b
#
# def \
#
#
# lcs_trackback(x,y):
#     c,b=lcs ( x ,y)
#     # print(b)
#     i=len( x )
#     j=len( y )
#     res=[]
#     while i>0 an d j>0:
#         if b[i][j]==1:
#             res.append(x[i-1])
#             i-=1
#             j-=1
#         elif b[i][j]==2:
#             i-=1
#         elif b[i][j]==3:
#             j-=1
#     return ''.join(reversed(res))
#
#
# print(lcs_trackback("ABCDAB","ACD" ))
#
