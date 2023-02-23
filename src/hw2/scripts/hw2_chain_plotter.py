#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
import math 
from hw2.msg import Chain2D 


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
        x= D * math.cos(theta) - 0 * math.sin(theta) + prev_joint[0] 
        y= D * math.sin(theta) + 0 * math.cos(theta) + prev_joint[1] 
        joint_positions.append([x,y])
        vertices=[]
        w=W/2
        l=L/2
        
        vertices.append([prev_joint[0] + diagonal_distance * math.cos(theta+1.571+.785), prev_joint[1] + diagonal_distance * math.sin(theta+1.571+.785)])
        vertices.append([prev_joint[0] + diagonal_distance * math.cos(theta+3.14+.785), prev_joint[1] +  diagonal_distance  * math.sin(theta+3.14+.785)])
        
        
        vertices.append([x + diagonal_distance  * math.cos(theta-.785), y + diagonal_distance  * math.sin(theta-.785)])
        vertices.append([x +  diagonal_distance * math.cos(theta+.785), y + diagonal_distance * math.sin(theta+.785)])
        
        link_vertices.append(vertices)
        link_vertices.append(vertices)



    return (joint_positions, link_vertices)

def get_link_indices_containing(v, config, W, L, D):
    """@type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
            and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
        @type W: float, representing the width of each link
        @type L: float, representing the length of each link
        @type D: float, the distance between the two points of attachment on each link

        return the subset of {1...m} that represents all the indices of the links that contain the given point v
    """

    # Get the positions of all the links in the kinematic chain
    link_positions = get_link_positions(config, W, L, D)
    
    # Initialize an empty list to store the indices of the links that contain the point
    link_indices = []
    
    # Iterate over all the links in the chain and check if the given point lies on the link
    for i in range(1, len(link_positions)):
        x1, y1 = link_positions[i-1]
        x2, y2 = link_positions[i]
        # Check if the point lies on the line segment between the two points
        if (min(x1, x2) <= v[0] <= max(x1, x2)) and (min(y1, y2) <= v[1] <= max(y1, y2)):
            link_indices.append(i)
    
    return link_indices


if __name__ == "__main__":
    chain = get_chain_msg()
    plot_chain(chain.config, chain.W, chain.L, chain.D)
