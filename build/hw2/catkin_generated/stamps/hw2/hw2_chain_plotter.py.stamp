#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
import math 
from hw2.msg import Chain2D 

RADIAN_90=1.571
RADIAN_45=.785
RADIAN_180=3.142

def get_chain_msg():
    """Return a message from the "chain_config" channel.

    This function will wait until a message is received.
    """
    # TODO: Implement this function
    rospy.init_node("listener", anonymous=True)
    msg = rospy.wait_for_message("linkconfigs", Chain2D)
    
    Chain2D.config=msg.config
    Chain2D.W=msg.W 
    Chain2D.L=msg.L 
    Chain2D.D=msg.D 

    return Chain2D

    # raise NotImplementedError


def plot_chain(config, W, L, D):
    """Plot a 2D kinematic chain A_1, ..., A_m

    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link
    """
    # v=(7,7)
    # print(get_link_indices_containing(v, config, W, L, D))

    (joint_positions, link_vertices) = get_link_positions(config, W, L, D)

    fig, ax = plt.subplots()
    plot_links(link_vertices, ax)
    plot_joints(joint_positions, ax)
    ax.axis("equal")
    plt.show()


def plot_links(link_vertices, ax):
    """Plot the links of a 2D kinematic chain A_1, ..., A_m on the axis ax

    @type link_vertices: a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """

    for vertices in link_vertices:
        x = [vertex[0] for vertex in vertices]
        y = [vertex[1] for vertex in vertices]

        x.append(vertices[0][0])
        y.append(vertices[0][1])
        ax.plot(x, y, "k-", linewidth=2)


def plot_joints(joint_positions, ax):
    """Plot the joints of a 2D kinematic chain A_1, ..., A_m on the axis ax

    @type joint_positions: a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
    """
    x = [pos[0] for pos in joint_positions]
    y = [pos[1] for pos in joint_positions]
    ax.plot(x, y, "k.", markersize=10)




def get_link_positions(config, W, L, D):
    """Compute the positions of the links and the joints of a 2D kinematic chain A_1, ..., A_m

    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link

    @return: a tuple (joint_positions, link_vertices) where
        * joint_positions is a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
        * link_vertices is a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """
    # TODO: Implement this function
    # raise NotImplementedError
    def get_diagonal_distance():
        w=W/2
        return math.sqrt(w*w + w*w)

    joint_positions=[[0,0]]
    link_vertices=[]
    new_randian=[0]
    diagonal_distance=get_diagonal_distance()
    for theta in config:

        prev_joint=joint_positions[-1]
        prev_link_theta=new_randian[-1]
        theta=theta+prev_link_theta
        new_randian.append(theta)
        # computing joint position...
        x= D * math.cos(theta) - 0 * math.sin(theta) + prev_joint[0] 
        y= D * math.sin(theta) + 0 * math.cos(theta) + prev_joint[1] 
        joint_positions.append([x,y])
        vertices=[]
        # computing four corners of each link...
        vertices.append([prev_joint[0] + diagonal_distance * math.cos(theta+RADIAN_90+RADIAN_45), prev_joint[1] + diagonal_distance * math.sin(theta+RADIAN_90+RADIAN_45)])
        vertices.append([prev_joint[0] + diagonal_distance * math.cos(theta + RADIAN_180 +RADIAN_45), prev_joint[1] +  diagonal_distance  * math.sin(theta+RADIAN_180+RADIAN_45)])
        vertices.append([x + diagonal_distance  * math.cos(theta-RADIAN_45), y + diagonal_distance  * math.sin(theta-RADIAN_45)])
        vertices.append([x +  diagonal_distance * math.cos(theta + RADIAN_45), y + diagonal_distance * math.sin(theta + RADIAN_45)])
        
        link_vertices.append(vertices)



    return (joint_positions, link_vertices)

def get_link_indices_containing(v, config, W, L, D):

    """
        @v type v: tuple(x,y), representing the location of a point
        @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
            and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
        @type W: float, representing the width of each link
        @type L: float, representing the length of each link
        @type D: float, the distance between the two points of attachment on each link

        return the subset of {1...m} that represents all the indices of the links that contain the given point v
    """

    # Get the positions of all the links in the kinematic chain
    (joint_position, link_positions) = get_link_positions(config, W, L, D)
    x, y = v 
    link_indices = []

    for i in range(0, len(link_positions)):
        all_link_positions=link_positions[i]

        # assign four corners of a link into four points
        x0, y0 = all_link_positions[0]
        x1, y1 = all_link_positions[1]
        x2, y2 = all_link_positions[2]
        x3, y3 = all_link_positions[3]
        
        # calculate the edge of among the corners of the links
        Edge_1=(x1-x0) * (y-y0) - (y1-y0) * (x-x0)
        Edge_2=(x2-x1) * (y-y1) - (y2-y1) * (x-x1)
        Edge_3=(x3-x2) * (y-y2) - (y3-y2) * (x-x2)
        Edge_4=(x0-x3) * (y-y3) - (y0-y3) * (x-x3)

        #  decide whether a point inside the four edges... 
        if (Edge_1 >= 0 and Edge_2 >= 0 and Edge_3 >= 0 and Edge_4 >= 0) or (Edge_1 <= 0 and Edge_2 <= 0 and Edge_3 <= 0 and Edge_4 <= 0):
            # +1 is added because link index starts from 1
            link_indices.append(i+1)
            
    return link_indices


if __name__ == "__main__":
    chain = get_chain_msg()
    plot_chain(chain.config, chain.W, chain.L, chain.D)


    
