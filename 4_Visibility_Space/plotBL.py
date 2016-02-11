import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
def sphere(ant1,ant2,A,E,D,L):
    # Create a sphere
    r = 6371 #km
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)

    # coordinate center baseline
    r0=r
    #L=np.radians(45.)
    phi0=np.pi/2-L
    theta0=0.

    x0 = r0*sin(phi0)*cos(theta0)
    y0 = r0*sin(phi0)*sin(theta0)
    z0 = r0*cos(phi0)

    b=D/1e3 #km
    rant1=r+ant1[2]
    rant2=r+ant2[2]

    ant1phi=phi0+np.arctan(b/2*cos(A)/r)
    ant2phi=phi0-np.arctan(b/2*cos(A)/r)

    ant1theta=theta0+np.arctan(b/2*sin(A)/r)
    ant2theta=theta0-np.arctan(b/2*sin(A)/r)

    xant1=rant1*sin(ant1phi)*cos(ant1theta)
    xant2=rant2*sin(ant2phi)*cos(ant2theta)

    yant1=rant1*sin(ant1phi)*sin(ant1theta)
    yant2=rant2*sin(ant2phi)*sin(ant2theta)

    zant1=rant1*cos(ant1phi)
    zant2=rant2*cos(ant2phi)

    #Set colours and render
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_title("Baseline seen from the source")
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)

    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='k',alpha=0.02, linewidth=1,shade=False)
    ax.plot_surface(x, y, z*0,  rstride=40, cstride=40, color='c', alpha=0.1, linewidth=0,shade=False)

    ax.scatter(x0,y0,z0,color="k",s=5)
    ax.scatter(xant1,yant1,zant1,color="b",s=20)
    ax.scatter(xant2,yant2,zant2,color="b",s=20)
    ax.plot([xant1,xant2],[yant1,yant2],[zant1,zant2],color="g",linewidth=2)

    ax.plot([0,0],[0,0],[-7000,7000.],'k')
    ax.plot([0,0],[-7000,7000.],[0,0],'k')
    ax.plot([-7000,7000.],[0,0],[0,0],'k')
    ax.plot([0,x0],[0,y0],[0,z0],'r',linewidth=2)

    ax.view_init(30,50)
    ax.set_xlim([-7000,7000])
    ax.set_ylim([-7000,7000])
    ax.set_zlim([-7000,7000])
    ax.set_xlabel("X (km)")
    ax.set_ylabel("Y (km)")
    ax.set_zlabel("Z (km)")
    ax.set_aspect("equal")
    plt.tight_layout()

def makecubeplot(u,v,w):
    max_range = np.array([u.max()-u.min(), v.max()-v.min(), w.max()-w.min()]).max()
    Ub = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(u.max()+u.min())
    Vb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(v.max()+v.min())
    Wb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(w.max()+w.min())
    # Comment or uncomment following both lines to test the fake bounding box:
    for ub, vb, wb in zip(Ub, Vb, Wb):
        ax.plot([ub], [vb], [wb], 'w')

def UV(u,v,w):
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot(u,v,w,'b')
    ax.plot(-u,-v,-w,'r')

    ax.set_xlabel("u (klambda)")
    ax.set_ylabel("v (klambda)")
    ax.set_zlabel("w (klambda)")
    ax.plot(u,v,'b--',zdir='w',zs=w.min())
    ax.plot(-u,-v,'r--',zdir='w',zs=w.min())

def UVellipse(u,v,w,a,b,v0):
    fig=plt.figure(0)
    
    e1=Ellipse(xy=np.array([0,v0]),width=2*a,height=2*b,angle=0)
    e2=Ellipse(xy=np.array([0,-v0]),width=2*a,height=2*b,angle=0)

    ax=fig.add_subplot(111,aspect="equal")

    ax.plot([0],[v0],"go")
    ax.plot([0],[-v0],"go")
    ax.plot(u[0],v[0],"bo")
    ax.plot(u[-1],v[-1],"bo")

    ax.plot(-u[0],-v[0],"ro")
    ax.plot(-u[-1],-v[-1],"ro")

    ax.add_artist(e1)
    e1.set_lw(1)
    e1.set_ls("--")
    e1.set_facecolor("w")
    e1.set_edgecolor("b")
    e1.set_alpha(0.5)
    ax.add_artist(e2)

    e2.set_lw(1)
    e2.set_ls("--")
    e2.set_facecolor("w")
    e2.set_edgecolor("r")
    e2.set_alpha(0.5)
    ax.plot(u,v,"b")
    ax.plot(-u,-v,"r")
    ax.hold('on')

