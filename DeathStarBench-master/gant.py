import plotly.express as px
import pandas as pd

# Créer le DataFrame des tâches
df = pd.DataFrame([
    dict(Task="Mise en place env. dev. et migration scripts", Start='2025-06-15', Finish='2025-06-30', Section="Mission 1 : ESXi"),
    dict(Task="Automatisation VMs et vSAN", Start='2025-07-01', Finish='2025-07-15', Section="Mission 1 : ESXi"),
    dict(Task="Installation cluster Kubernetes", Start='2025-07-16', Finish='2025-07-31', Section="Mission 2 : Kubernetes"),
    dict(Task="Déploiement DeathStarBench", Start='2025-08-01', Finish='2025-08-20', Section="Mission 2 : Kubernetes"),
    dict(Task="Injection de charge et monitoring Grafana", Start='2025-08-21', Finish='2025-09-05', Section="Mission 2 : Kubernetes"),
    dict(Task="Tests finaux et rédaction rapport", Start='2025-09-06', Finish='2025-09-12', Section="Clôture"),
])

# Créer le diagramme de Gantt
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Section", color="Section", text="Task")

# Inverser l'axe y pour que la première tâche soit en haut
fig.update_yaxes(autorange="reversed")

# Améliorer le style
fig.update_layout(title="Planning du stage", xaxis_title="Dates", yaxis_title="", showlegend=False)

# Afficher
fig.show()
