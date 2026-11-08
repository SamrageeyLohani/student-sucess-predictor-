import numpy as np 
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)
n = 1000

#hidden trait
ability = rng.normal(0,1,n)
engagement = 0.3 * ability +rng.normal(0, 0.95, n)


print("First 5 ability values:", ability[:5].round(2)) #round means two decimal places and ability means first 5 items
print("Correlation:", np.corrcoef(ability, engagement)[0, 1].round(2)) 
#np.corrcoef returns a small 2×2 table of correlations between every pair of inputs. The number you want is the relationship between the two different variables, which sits at position [0, 1] (row 0, column 1). Correlation runs from -1 to 1:

#plotting
plt.scatter(ability, engagement, alpha = 0.4) #puts one dot per student, with ability left-to-right and engagement bottom-to-top.
#alpha makes dots semi-transparent, so overlapping dots look darker and you can see where students cluster.
plt.xlabel("ability") #label the axes.
plt.ylabel("engagement") #label the axes.
plt.show() #opens the window. Nothing appears until this line runs.
