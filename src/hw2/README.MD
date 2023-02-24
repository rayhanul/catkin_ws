


# This ros package named hw2 can rotate and translate different links based on the input values. 


In order run this package, you must have ROS noetic installed in your computer. Due to the dependencies, Linux based OS such as Ubuntu is preferable. 

Once you have ROS installed in your computer, run following command to go to ros package. 

```
roscd hw2
``` 
To install this package, go the catkin directory and run the following command 

```
catkin_make 
``` 

After that, open another terminal and run "roscore" command to your terminal. 

Then run the following command in another terminal 

```
rosrun hw2 hw2_chain_configurator.py  0.7853981633974483 1.5707963267948966 -0.7853981633974483 -W 2 -L 12 -D 10
```

After that you can able to see output by running the following command in another terminal. 

``` 
rosrun hw2 hw2_chain_plotter.py
``` 


In order to check the function get_link_indices_containing(v, config, W, L, D), please uncomment lines 36 and 37 in plot_chain() function. 

**Example: v=(7,7), get_link_indices_containing(v, config, W, L, D) returns [1,2] where links index starts from 1.**
