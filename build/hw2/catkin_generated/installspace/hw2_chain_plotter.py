#!/usr/bin/env python3
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

    joint_positions=[[0,0]]
    link_vertices=[]

    for theta in config:

        # prev_joint=joint_positions[-1]
        # x=prev_joint[0] + D * math.cos(theta) 
        # y=prev_joint[1] + D * math.sin(theta)
        # joint_positions.append([x,y])
        # vertices=[]
        # w=W/2
        # l=L/2

        # vertices.append([prev_joint[0] + w * math.sin(theta), prev_joint[1] - w * math.cos(theta)])
        # vertices.append([prev_joint[0] - w * math.sin(theta), prev_joint[1] + w * math.cos(theta)])
        # vertices.append([x - w * math.sin(theta), y + w * math.cos(theta)])
        # vertices.append([x + w * math.sin(theta), y - w * math.cos(theta)])
        # link_vertices.append(vertices)

        prev_joint=joint_positions[-1]
        x=(prev_joint[0] * math.cos(theta) - prev_joint[1] * math.sin(theta)) + D 
        y=(prev_joint[0] * math.sin(theta) + prev_joint[1] * math.cos(theta)) + 0 
        joint_positions.append([x,y])
        vertices=[]
        w=W/2
        l=L/2

        vertices.append([prev_joint[0] + w * math.sin(theta), prev_joint[1] - w * math.cos(theta)])
        vertices.append([prev_joint[0] - w * math.sin(theta), prev_joint[1] + w * math.cos(theta)])
        vertices.append([x - w * math.sin(theta), y + w * math.cos(theta)])
        vertices.append([x + w * math.sin(theta), y - w * math.cos(theta)])
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

    raise NotImplementedError


if __name__ == "__main__":
    chain = get_chain_msg()
    plot_chain(chain.config, chain.W, chain.L, chain.D)
