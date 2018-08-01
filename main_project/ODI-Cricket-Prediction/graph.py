import matplotlib.pyplot as mt
import numpy as np
def graphofplayer(ty,name):
    if ty=="batsman":
        x,y=np.loadtxt('D:/ODIPrediction/main_project/ODI-Cricket-Prediction/statforgraph/'+name+'.csv',delimiter=',',unpack=True)
        #mt.subplot(211)
        mt.bar(x,y,color=['orange'])
        mt.xlabel('YEAR')
        mt.ylabel('RUNS')

        mt.legend()
        mt.savefig('static/graph/' + name + '1.png')
        #mt.show()
        #mt.subplot(212)
        #mt.scatter(x,y,color=['red','green','blue'])
        #mt.xlabel('YEAR')
        #mt.ylabel('RUNS')
        #mt.grid()
        #mt.title(name)
        #mt.legend()
        #mt.savefig('static/' + name + '1.png')
        #mt.show()

    else:
        x,y=np.loadtxt('D:/ODIPrediction/main_project/ODI-Cricket-Prediction/statforgraph/'+name+'.csv',delimiter=',',unpack=True)
        #mt.subplot(2,1,1)
        mt.bar(x,y,color=['orange'])
        mt.xlabel('YEAR')
        mt.ylabel('WICKETS')

        mt.legend()
        mt.savefig('static/graph/' + name + '1.png')
        #mt.show()
        #mt.subplot(2,1,2)
        #mt.scatter(x,y,color=['red','green','blue'])
        #mt.xlabel('YEAR')
        #mt.ylabel('WICKETS')
        #mt.grid()
        #mt.title(name)
        #mt.legend()
        #mt.show()
