import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("load_data.csv")

# core
df_feed =  df[df["ga:pagePathLevel1"].str.contains("/newsfeed")]
df_wire = df[df["ga:pagePathLevel1"].str.contains("/thewire")]
df_groups = df[df["ga:pagePathLevel1"].str.contains("/groups")]
df_profile = df[df["ga:pagePathLevel1"].str.contains("/profile")]
df_dashboard = df[df["ga:pagePathLevel1"].str.contains("/dashboard")]
df_activity = df[df["ga:pagePathLevel1"].str.contains("/activity")]
df_members = df[df["ga:pagePathLevel1"].str.contains("/members")]
df_questions = df[df["ga:pagePathLevel1"].str.contains("/questions")]
df_missions = df[df["ga:pagePathLevel1"].str.contains("/missions")]
df_bookmarks = df[df["ga:pagePathLevel1"].str.contains("/bookmarks")]
df_discussion = df[df["ga:pagePathLevel1"].str.contains("/discussion/")]
df_blogs = df[df["ga:pagePathLevel1"].str.contains("/blog")]
df_polls = df[df["ga:pagePathLevel1"].str.contains("/polls")]
df_events = df[df["ga:pagePathLevel1"].str.contains("/event_calendar/")]
df_files = df[df["ga:pagePathLevel1"].str.contains("/file")]
df_help = df[df["ga:pagePathLevel1"].str.contains("/help")]
# Communities
df_atip = df[df["ga:pagePathLevel1"].str.contains("/ATIP_AIPRP")]
df_communications = df[df["ga:pagePathLevel1"].str.contains("/Communications")] 
df_evaluators = df[df["ga:pagePathLevel1"].str.contains("/Evaluators_Évaluateurs")]
df_finance = df[df["ga:pagePathLevel1"].str.contains("/Finance")]  # Financial Officers
df_HR = df[df["ga:pagePathLevel1"].str.contains("/HR_RH")] 
df_info_mgmt = df[df["ga:pagePathLevel1"].str.contains("/IM_GI")]  
df_IT = df[df["ga:pagePathLevel1"].str.contains("/Information")]  
df_audit = df[df["ga:pagePathLevel1"].str.contains("/Auditors_Vérificateurs")]  
df_material_mgmt = df[df["ga:pagePathLevel1"].str.contains("/Material_matériel")]  
df_policy = df[df["ga:pagePathLevel1"].str.contains("/Policy_Politiques")]  
df_procurement = df[df["ga:pagePathLevel1"].str.contains("/Procurement_Acquisitions")]  
df_real_property = df[df["ga:pagePathLevel1"].str.contains("/RealProperty_BiensImmobiliers")]  # ATIP specialists
df_regulators = df[df["ga:pagePathLevel1"].str.contains("/Regulators_Régulateurs")]  # ATIP specialists
df_science = df[df["ga:pagePathLevel1"].str.contains("/Science_Tech")]  # ATIP specialists
df_security = df[df["ga:pagePathLevel1"].str.contains("/Security_Sécurité")]  # ATIP specialists
df_service = df[df["ga:pagePathLevel1"].str.contains("/Service")]  # ATIP specialists

print(df_wire)

communities = [
  ["ATIP Specialists", len(df_atip["ga:pageLoadTime"]), df_atip["ga:pageLoadTime"].mean()],
  ["Communications", len(df_communications["ga:pageLoadTime"]),  df_communications["ga:pageLoadTime"].mean()],
  ["Evaluators", len(df_evaluators["ga:pageLoadTime"]),  df_evaluators["ga:pageLoadTime"].mean()],
  ["Finance", len(df_finance["ga:pageLoadTime"]),  df_finance["ga:pageLoadTime"].mean()],
  ["Human Resources", len(df_HR["ga:pageLoadTime"]),  df_HR["ga:pageLoadTime"].mean()],
  ["Information Management", len(df_info_mgmt["ga:pageLoadTime"]),  df_info_mgmt["ga:pageLoadTime"].mean()],
  ["Information Technology", len(df_IT["ga:pageLoadTime"]),  df_IT["ga:pageLoadTime"].mean()],
  ["Audit", len(df_audit["ga:pageLoadTime"]),  df_audit["ga:pageLoadTime"].mean()],
  ["Material Management", len(df_material_mgmt["ga:pageLoadTime"]),  df_material_mgmt["ga:pageLoadTime"].mean()],
  ["Policy", len(df_policy["ga:pageLoadTime"]),  df_policy["ga:pageLoadTime"].mean()],
  ["Procurement", len(df_procurement["ga:pageLoadTime"]),  df_procurement["ga:pageLoadTime"].mean()],
  ["Real Property", len(df_real_property["ga:pageLoadTime"]),  df_real_property["ga:pageLoadTime"].mean()],
  ["Regulatord", len(df_regulators["ga:pageLoadTime"]),  df_regulators["ga:pageLoadTime"].mean()],
  ["Science and Technology", len(df_science["ga:pageLoadTime"]),  df_science["ga:pageLoadTime"].mean()],
  ["Security", len(df_security["ga:pageLoadTime"]),  df_security["ga:pageLoadTime"].mean()],
  ["Service", len(df_service["ga:pageLoadTime"]),  df_service["ga:pageLoadTime"].mean()]
]

other = [
    ["Newsfeed", len(df_feed["ga:pageLoadTime"]),  df_feed["ga:pageLoadTime"].mean()],
    ["The Wire", len(df_wire["ga:pageLoadTime"]),  df_wire["ga:pageLoadTime"].mean()],
    ["Groups", len(df_groups["ga:pageLoadTime"]),  df_groups["ga:pageLoadTime"].mean()],
    ["Profile", len(df_profile["ga:pageLoadTime"]),  df_profile["ga:pageLoadTime"].mean()],
    ["Dashboard", len(df_dashboard["ga:pageLoadTime"]),  df_dashboard["ga:pageLoadTime"].mean()],
    ["Activity", len(df_activity["ga:pageLoadTime"]),  df_activity["ga:pageLoadTime"].mean()],
    ["Members", len(df_members["ga:pageLoadTime"]),  df_members["ga:pageLoadTime"].mean()],
    ["Questions", len(df_questions["ga:pageLoadTime"]),  df_questions["ga:pageLoadTime"].mean()],
    ["Missions", len(df_missions["ga:pageLoadTime"]),  df_missions["ga:pageLoadTime"].mean()],
    ["Bookmarks", len(df_bookmarks["ga:pageLoadTime"]),  df_bookmarks["ga:pageLoadTime"].mean()],
    ["Discussions", len(df_discussion["ga:pageLoadTime"]),  df_discussion["ga:pageLoadTime"].mean()],
    ["Blogs", len(df_blogs["ga:pageLoadTime"]),  df_blogs["ga:pageLoadTime"].mean()],
    ["Polls", len(df_polls["ga:pageLoadTime"]),  df_polls["ga:pageLoadTime"].mean()],
    ["Events", len(df_events["ga:pageLoadTime"]),  df_events["ga:pageLoadTime"].mean()],
    ["Files", len(df_files["ga:pageLoadTime"]),  df_files["ga:pageLoadTime"].mean()],
    ["Help", len(df_help["ga:pageLoadTime"]),  df_help["ga:pageLoadTime"].mean()]
]
fig, ax = plt.subplots()


df_communities = pd.DataFrame(communities)
df_communities.columns = ["name",  "sample_size",  "mean"]
df_communities["mean"] = df_communities["mean"]/1000 # convert to seconds

df_communities.plot.scatter(x="sample_size", y="mean", style=".",  label="Community", ax=ax, color="red")
# add labels to scatter plot dots
'''
for i, community in enumerate(df_communities["name"]):
    ax.annotate(community, (df_communities["sample_size"][i], df_communities["mean"][i] + 0.5))
'''

df_other = pd.DataFrame(other)
df_other.columns = ["name",  "sample_size",  "mean"]
df_other["mean"] = df_other["mean"]/1000 # convert to seconds

df_other.plot.scatter(x="sample_size", y="mean", style=".",  label="Other Feature", ax=ax)
# add labels to scatter plot dots
for i, feature in enumerate(df_other["name"]):
    ax.annotate(feature, (df_other["sample_size"][i], df_other["mean"][i] + 0.5))

plt.xlabel("Sample Size ( % of the # of visits )")
plt.ylabel("Average Load Time")

plt.title("Average Load Time vs. Usage of Platform Features")

plt.show()