
# coding: utf-8

# # Plotting with Matplotlib
# Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# In[8]:


# Import necessary packages and load `winequality_edited.csv`
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('winequality_edited.csv')


# ### #1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# In[9]:


# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[10]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# ### #2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# In[14]:


# Use query to select each group and get its mean quality
median_sugar = df['residual_sugar'].median()
low_sugar = df.query('residual_sugar < {}'.format(median_sugar))
high_sugar = df.query('residual_sugar >= {}'.format(median_sugar))

mean_quality_low_sugar = low_sugar['quality'].mean()
mean_quality_high_sugar = high_sugar['quality'].mean()


# In[19]:


# Create a bar chart with proper labels
locations = [1,2]
heights = [mean_quality_low_sugar, mean_quality_high_sugar]
labels = ['Low Sugar', 'High Sugar']
plt.bar(locations, heights, tick_label = labels)
plt.title('Quality of Wines by Sugar Content')
plt.xlabel('Sugar Content')
plt.ylabel('Average Quality Rating')


# ### #3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# In[29]:


# Use groupby to get the mean quality for each acidity level
acid_means = df.groupby('acidity_levels')['quality'].mean()
print(acid_means)


# In[22]:


df.head()


# In[31]:


# Create a bar chart with proper labels
locations = [1,2,3,4]
heights = acid_means
labels = ['low', 'medium', 'moderate','high']
plt.bar(locations, heights, tick_label = labels)
plt.title('Quality by Acidity')
plt.xlabel('Acidity Level')
plt.ylabel('Average Quality')


# ### Bonus: Create a line plot for the data in #3
# You can use pyplot's [plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) function for this.

# In[32]:


plot(acid_means)


# Compare this with the bar chart. How might showing this visual instead of the bar chart affect someone's conclusion about this data?
