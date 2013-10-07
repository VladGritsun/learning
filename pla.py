from random import *

def gen_line() :
    r = random()
    if r < 0.25 :
        return (random(),random(),0)
    elif r < 0.5 :
        return (-random(),random(),0)
    elif r < 0.75 :
        return (-random(),-random(),0)
    else :
        return (-random(),-random(),0)
        
        
def gen_points(N,line) :
    points,labels = [],[]
    for i in range(N) :
        r = random()
        p = (0,0,1)
        if r < 0.25 :
            p= (random(),random(),1)
        elif r < 0.5 :
            p= (-random(),random(),1)
        elif r < 0.75 :
            p= (-random(),-random(),1)
        else :
            p= (-random(),-random(),1)
        points.append(p)
        labels.append(p[0]*line[0]+p[1]*line[1]+p[2]*line[2])
    return points,labels


# points are the tuples in 2-d space
def pla(points,labels) :
    z = (0,0,0)
    iters = 0
    while True :
        miscl_p = []
        miscl_l = []
        for i,p in enumerate(points) :
            cur_label = z[0]*p[0]+z[1]*p[1]+z[2]*p[2]
            if labels[i]* cur_label <= 0 :
                miscl_p.append(p)
                miscl_l.append(labels[i])
        l = len(miscl_p)
        if l == 0 :
            break
        #print miscl_p
        i = randint(0,l-1)
        a,b,c = miscl_p[i][0], miscl_p[i][1], miscl_p[i][2]
        if miscl_l[i] >= 0 :
            new_z = (z[0]+a,z[1]+b,z[2]+c)
            z = new_z
        else :
            new_z = (z[0]-a,z[1]-b,z[2]-c)
            z = new_z
        iters += 1
        
    return z,iters

def classify(points,line) :
    labels = []
    for p in points :
        labels.append(p[0]*line[0]+p[1]*line[1]+p[2]*line[2])
    return labels

def num_misclassified(labels1,labels2) :
    res = 0
    for i in range(len(labels1)) :
        if labels1[i]*labels2[i] <= 0 :
            res+=1
            
    return res

def experiment(N) :
    iter_list = []
    miscl_list = []
    for i in range(1000) :
        line = gen_line()
        points,labels = gen_points(N,line)
        z,iters = pla(points,labels)
        
        new_points,labels_z = gen_points(1000,z)
        labels_l = classify(new_points,line)
        miscl = num_misclassified(labels_z,labels_l)
        
        miscl_list.append(miscl/1000.0)
        iter_list.append(iters)
        
        
    print "ITERS " + str(sum(iter_list)/len(iter_list))
    print "MISC " + str(sum(miscl_list)/len(miscl_list))
        

                
    
