fig, axs = plt.subplots(1, 1, figsize=(12,4), sharex=False)

axs.plot(df.index, df["YY_Obs"], '-b', lw=1, label='Observation')
axs.plot(df.index, df["YY_Sim"], 'r--', lw=1, label='Prevision 1J')
axs.legend(fontsize = 10, ncols=2, frameon=False, loc="best");
axs.set_ylabel("Q($m^3/s$)", fontsize=9)
plt.tight_layout()


# # Critère d'évaluation
# NSE = he.evaluator(he.nse, df["YY_Sim"], df["YY_Obs"])
# KGE, r, alpha, beta = he.evaluator(he.kge, df["YY_Sim"], df["YY_Obs"])
# print("NSE:", round(NSE[0], 2))
# print("KGE:", round(KGE[0], 2))