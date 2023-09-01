############################################
#Make boxplot
############################################

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

datab1_inve = bed_mobility_inve[0:32]
datab2_inve = bed_mobility_inve[32:54]
datab3_inve = bed_mobility_inve[55:79]
data_to_plot_inve = [datab3_inve, datab2_inve, datab1_inve ]
bp_inve = axes[0].boxplot(data_to_plot_inve, patch_artist=True, boxprops=dict(facecolor='white'))
for patch, color in zip(bp_inve['boxes'], box_colors):
    patch.set_facecolor(color)
axes[0].set_xticklabels(['River mouth\nInner-shelf (Z1)', 'Inner-shelf  (Z2)', 'Outer-shelf (Z3)'])
axes[0].set_ylabel('%')

axes[0].text(-0.05, 1.05, "a)", transform=axes[0].transAxes, fontsize=12, fontweight='bold')

datab1_prim = bed_mobility_prim[0:32]
datab2_prim = bed_mobility_prim[32:54]
datab3_prim = bed_mobility_prim[55:79]
data_to_plot_prim = [datab3_prim, datab2_prim, datab1_prim]
bp_prim = axes[1].boxplot(data_to_plot_prim, patch_artist=True, boxprops=dict(facecolor='white'))
for patch, color in zip(bp_prim['boxes'], box_colors):
    patch.set_facecolor(color)
axes[1].set_xticklabels(['River mouth\nInner-shelf (Z1)', 'Inner-shelf  (Z2)', 'Outer-shelf (Z3)'])
axes[1].set_ylabel('%')

axes[1].text(-0.05, 1.05, "b)", transform=axes[1].transAxes, fontsize=12, fontweight='bold')

plt.tight_layout()

plt.show()
print(np.mean(datab1_prim),np.mean(datab2_prim), np.mean(datab3_prim),np.mean(datab1_inve),np.mean(datab2_inve), np.mean(datab3_inve))
#datab1 = tm_prim[:,0:32]
#datab2 = tm_prim[:,32:54]
#datab3 = tm_prim[:,55:79]
#datab1=datab1.flatten()
#datab2=datab2.flatten()
#datab3=datab3.flatten()


