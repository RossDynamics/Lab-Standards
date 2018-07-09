# We typically use Matplotlib and seaborn to make plots look pretty
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('ticks')

# Define font styles as dictionaries
titlefont = {'fontsize':12,'family':'serif','fontname':'Computer Modern'}
labelfont = {'fontsize':10,'family':'serif','fontname':'Computer Modern'}
tickfont = {'fontsize':8,'family':'serif','fontname':'Computer Modern'}

# Generate Plot
plt.figure(figsize=(3.6, 2.4)) # Set the size it will be in the document
# figsize=(width, height)
plt.title('This is the title', **titlefont)
plt.xlabel('$x$-axis label', **labelfont)
plt.ylabel('$y$-axis label', **labelfont)
plt.yticks([-1.0, -0.5, 0], **tickfont)
plt.xticks([-1.0, 0, 1.0], **tickfont)

##Set Limits
# Predefined limits
plt.xlim([0, 21])
plt.ylim([-1.15, 0])

# Autoscaled
plt.autoscale(enable=True, axis='x', tight=True)

# Equal Axes
ax = plt.gca()
ax.set_aspect('equal', adjustable='box', anchor='C')
# Note that axes should be equal when both directions represent the same
#    quantity over a similar scale

# Save a Figure
plt.savefig('/path/to/name.eps', transparent=True, bbox_inches='tight')