#Define fonts
titlefont = {'fontsize':12,'family':'serif','fontname':'Times New Roman'}
labelfont = {'fontsize':10,'family':'serif','fontname':'Times New Roman'}
tickfont = {'fontsize':8,'family':'serif','fontname':'Times New Roman'}
sns.set_style('ticks')

#Generate Plot
plt.figure(figsize=(3.6, 1.8))
plt.xlabel('Streamwise spacing, $x^*$', **labelfont)
plt.ylabel('Regression Coefficient', **labelfont)
plt.yticks([-1.0, -0.5, 0], **tickfont)
plt.xticks([0, 5, 10, 15, 20], **tickfont)

##Set Limits
#Predefined limits
plt.xlim([0, 21])
plt.ylim([-1.15, 0])

#Equal Axes
ax = plt.gca()
ax.set_aspect('equal', adjustable='box', anchor='C')

#Autoscaled
plt.autoscale(enable=True, axis='x', tight=True)
