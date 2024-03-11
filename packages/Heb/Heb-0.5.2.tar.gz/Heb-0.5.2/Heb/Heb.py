class Heb:
    def p1(self):
        print('''
class McCullochPittsNeuron: 
    def __init__(self, weights, threshold): 
        self.weights = weights 
        self.threshold = threshold 

    def activate(self, inputs): 
        weighted_sum = sum([inputs[i] * self.weights[i] for i in range(len(inputs))]) 
        return 1 if weighted_sum >= self.threshold else 0 

# AND Logic Function 
and_weights = [1, 1] 
and_threshold = 2 
and_neuron = McCullochPittsNeuron(and_weights, and_threshold) 

# OR Logic Function 
or_weights = [1, 1] 
or_threshold = 1 
or_neuron = McCullochPittsNeuron(or_weights, or_threshold) 

# Test AND logic function 
input_values_and = [(0, 0), (0, 1), (1, 0), (1, 1)] 
print("AND Logic Function:") 
for inputs in input_values_and: 
    output = and_neuron.activate(inputs) 
    print(f"Input: {inputs}, Output: {output}") 

# Test OR logic function 
input_values_or = [(0, 0), (0, 1), (1, 0), (1, 1)] 
print("\n OR Logic Function:") 
for inputs in input_values_or: 
    output = or_neuron.activate(inputs) 
    print(f"Input: {inputs}, Output: {output}")
    
        ''')
    def p2(self):
        print(''' 
class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        weighted_sum = sum([inputs[i] * self.weights[i] for i in range(len(inputs))])
        return 1 if weighted_sum >= self.threshold else 0

and_not_weights = [1, -1]
and_not_threshold = 1
and_not_neuron = McCullochPittsNeuron(and_not_weights, and_not_threshold)

input_values_and_not = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("And not")
for inputs in input_values_and_not:
    outputs = and_not_neuron.activate(inputs)
    print(f"Input={inputs}, Output={outputs}")

xor_weights = [1, 1]
xor_threshold = 2
xor_neuron = McCullochPittsNeuron(xor_weights, xor_threshold)

or_weights = [1, 1]
or_threshold = 1
or_neuron = McCullochPittsNeuron(or_weights, or_threshold)

nand_weights = [-1, -1]
nand_threshold = -1
nand_neuron = McCullochPittsNeuron(nand_weights, nand_threshold)

input_values_xor = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("XOR")
for inputs in input_values_xor:
    nand_output = nand_neuron.activate(inputs)
    or_output = or_neuron.activate(inputs)
    outputs = xor_neuron.activate((nand_output, or_output))
    print(f"Input={inputs}, Output={outputs}")
              
              ''')
    def p3(self):
        print('''

import numpy as np
def initialize_weights_and_threshold(num_features):
    weights = np.random.rand(num_features + 1)
    threshold = 0
    return weights, threshold
def perceptron_train(inputs, targets, weights, threshold, learning_rate, max_iterations=1000):
    converged = False
    num_iterations = 0   
    while not converged and num_iterations < max_iterations:
        num_iterations += 1
        converged = True      
        for input_data, target in zip(inputs, targets):
            input_data_with_bias = np.insert(input_data, 0, 1)          
            weighted_sum = np.dot(weights, input_data_with_bias)           
            output = 1 if weighted_sum > threshold else 0           
            if output != target:
                converged = False
                weights += learning_rate * (target - output) * input_data_with_bias       
            print(f"Input: {input_data_with_bias}, Weighted Sum: {weighted_sum}")         
    return weights, num_iterations
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([0, 0, 0, 1])
num_features = len(inputs[0])
weights, threshold = initialize_weights_and_threshold(num_features)
learning_rate = 0.1
trained_weights, num_iterations = perceptron_train(inputs, targets, weights, threshold, learning_rate)
print(f"Converged in {num_iterations} iterations")
print("Trained Weights:", trained_weights)


''')
    def p4(self):
        print('''
import numpy as np
import matplotlib.pyplot as plt

class HebbianNetwork:
    def __init__(self, input_size):
        self.weights = np.zeros((input_size, input_size))

    def train(self, input_patterns):
        for pattern in input_patterns:
            self.weights += np.outer(pattern, pattern)

    def classify(self, input_pattern):
        output = np.dot(input_pattern, self.weights)
        return np.sign(output)

def plot_patterns(input_patterns, title):
    for pattern in input_patterns:
        plt.scatter(pattern[0], pattern[1], color='b')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()

def main():
    input_size = 2
    hebb_net = HebbianNetwork(input_size)

    # Define input patterns
    pattern1 = np.array([1, 1])
    pattern2 = np.array([1, -1])
    pattern3 = np.array([-1, 1])
    pattern4 = np.array([-1, -1])

    input_patterns = [pattern1, pattern2, pattern3, pattern4]

    # Train the Hebbian network
    hebb_net.train(input_patterns)

    # Classify new patterns
    test_pattern1 = np.array([0.5, 0.5])
    test_pattern2 = np.array([0.5, -0.5])
    test_pattern3 = np.array([-0.5, 0.5])
    test_pattern4 = np.array([-0.5, -0.5])

    result1 = hebb_net.classify(test_pattern1)
    result2 = hebb_net.classify(test_pattern2)
    result3 = hebb_net.classify(test_pattern3)
    result4 = hebb_net.classify(test_pattern4)

    print(f"Test Pattern 1 Result: {result1}")
    print(f"Test Pattern 2 Result: {result2}")
    print(f"Test Pattern 3 Result: {result3}")
    print(f"Test Pattern 4 Result: {result4}")

    # Plot input patterns and test patterns
    plot_patterns(input_patterns, 'Input Patterns')
    plot_patterns([test_pattern1, test_pattern2, test_pattern3, test_pattern4], 'Test Patterns')

if __name__ == "__main__":
    main()
''')
    def p5(self):
        print('''
        import numpy as np


class DiscreteFieldNetwork:
    def __init__(self,num_nueron):
        self.num_nueron=num_nueron
        self.weight=np.zeros((num_nueron,num_nueron))
    def train(self,patterns):
        pattern=np.array(patterns)
        outer_product=np.outer(pattern,pattern)
        np.fill_diagonal(outer_product,0)
        self.weight+=outer_product
    def energy(self,state):
        state=np.array(state)
        return 0.5*np.sign(np.dot(self.weight,state))
    def update_rule(self,state):
        new_state=np.sign(np.dot(self.weight,state))
        new_state[new_state>=0]=1
        new_state[new_state<0]=0
        return new_state
    def run(self,initial_state,max_iteration=100):
        current_state=np.array(initial_state)
        for _ in range(max_iteration):
            new_state=self.update_rule(current_state)
            if np.array_equal(new_state,current_state):
                break
        current_state=new_state
        return current_state

hopfield_network=DiscreteFieldNetwork(4)
training_pattern=[[1,1,1,-1]]
hopfield_network.train(training_pattern)
initial_state=[0,0,1,0]
result=hopfield_network.run(initial_state)
print(result)
print("energy:",hopfield_network.energy(result))

''')
    def p6(self):
        print('''
import numpy as np
import matplotlib.pyplot as plt

class KohonenSOM:
    def __init__(self, input_size, map_size):
        self.input_size = input_size
        self.map_size = map_size
        self.weights = np.random.rand(map_size[0], map_size[1], input_size)

    def update_weights(self, input_vector, winner, learning_rate, neighborhood_radius):
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight_vector = self.weights[i, j, :]
                distance = np.linalg.norm(np.array([i, j]) - np.array(winner))
                influence = np.exp(-(distance*2) / (2 * neighborhood_radius*2))
                self.weights[i, j, :] += learning_rate * influence * (input_vector - weight_vector)

    def train(self, data, epochs, initial_learning_rate=0.1, initial_radius=None):
        if initial_radius is None:
            initial_radius = max(self.map_size) / 2

        for epoch in range(epochs):
            learning_rate = initial_learning_rate * np.exp(-epoch / epochs)
            neighborhood_radius = initial_radius * np.exp(-epoch / epochs)

            for input_vector in data:
                winner = self.find_winner(input_vector)
                self.update_weights(input_vector, winner, learning_rate, neighborhood_radius)

    def find_winner(self, input_vector):
        min_distance = float('inf')
        winner = (0, 0)

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight_vector = self.weights[i, j, :]
                distance = np.linalg.norm(input_vector - weight_vector)

                if distance < min_distance:
                    min_distance = distance
                    winner = (i, j)

        return winner

    def visualize(self, data):
        colors = ['r', 'g', 'b', 'y', 'c', 'm']

        for input_vector in data:
            winner = self.find_winner(input_vector)
            plt.scatter(winner[0], winner[1], color=colors[np.random.randint(len(colors))])

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                plt.scatter(i, j, color='k', marker='x')

        plt.show()

# Example usage:
if __name__ == "__main__":
    # Generate some random 2D data points
    data = np.random.rand(100, 2)

    # Create a Kohonen SOM with input size 2 and a 10x10 map
    som = KohonenSOM(input_size=2, map_size=(10, 10))

    # Train the SOM for 100 epochs
    som.train(data, epochs=100)

    # Visualize the result
    som.visualize(data)''')
    def p7(self):
        print('''
import numpy as np
import matplotlib.pyplot as plt
class LVQ:
    def __init__(self, input_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.weights = np.random.rand(output_size, input_size)
    def find_winner(self, data_point):
        distances = np.linalg.norm(self.weights - data_point, axis=1)
        winner_index = np.argmin(distances)
        return winner_index
    def update_weights(self, data_point, winner_index, target):
        learn_rate = self.learning_rate
        self.weights[winner_index] += learn_rate * (data_point - self.weights[winner_index])
    def train(self, data, targets, epochs=100):
        for epoch in range(epochs):
            for i in range(len(data)):
                data_point = data[i]
                target = targets[i]
                winner_index = self.find_winner(data_point)
                self.update_weights(data_point, winner_index, target)
    def predict(self, data):
        predictions = []
        for data_point in data:
            winner_index = self.find_winner(data_point)
            predictions.append(winner_index)
        return np.array(predictions)
np.random.seed(42)
class_0 = np.random.rand(50, 2) * 0.5
class_1 = 0.5 + np.random.rand(50, 2) * 0.5
data = np.concatenate((class_0, class_1))
labels = np.concatenate((np.zeros(50), np.ones(50)))
lvq_model = LVQ(input_size=2, output_size=2, learning_rate=0.01)
lvq_model.train(data, labels, epochs=100)
test_data = np.random.rand(10, 2)
predictions = lvq_model.predict(test_data)
plt.scatter(class_0[:,0], class_0[:,1], color='blue', label='Class 0')
plt.scatter(class_1[:,0], class_1[:,1], color='red', label='Class 1')
plt.scatter(test_data[:,0], test_data[:,1], color='green', marker='o', label='Test Data')
for i in range(lvq_model.output_size):
    plt.plot([lvq_model.weights[i,0]], [lvq_model.weights[i,1]], marker='x')
plt.title('LVQ Classification')
plt.legend()
plt.show()



''')
    
    def p8(self):
        print('''                      
import numpy as np

def bipolar_sigmoid(x):
    return 2 / (1 + np.exp(-x)) - 1

def bipolar_sigmoid_derivative(x):
    return 0.5 * (1 + x) * (1 - x)

def initialize_weights(input_size, hidden_size, output_size):
    np.random.seed(42)
    weights_input_hidden = np.random.rand(input_size, hidden_size) - 0.5  # Transpose here
    weights_hidden_output = np.random.rand(output_size, hidden_size) - 0.5
    return weights_input_hidden, weights_hidden_output

def forward_propagation(inputs, weights_input_hidden, weights_hidden_output):
    hidden_inputs = np.dot(inputs, weights_input_hidden.T)  # Transpose inputs here
    hidden_outputs = bipolar_sigmoid(hidden_inputs)

    final_inputs = np.dot(hidden_outputs, weights_hidden_output.T)  # Transpose weights here
    final_outputs = bipolar_sigmoid(final_inputs)

    return hidden_outputs, final_outputs

def backward_propagation(inputs, targets, hidden_outputs, final_outputs, weights_hidden_output):
    output_errors = targets - final_outputs
    output_gradients = bipolar_sigmoid_derivative(final_outputs) * output_errors

    hidden_errors = np.dot(weights_hidden_output.T, output_gradients)
    hidden_gradients = bipolar_sigmoid_derivative(hidden_outputs) * hidden_errors

    return output_gradients, hidden_gradients

def update_weights(inputs, hidden_outputs, output_gradients, hidden_gradients,
                   weights_input_hidden, weights_hidden_output, learning_rate):
    weights_hidden_output += learning_rate * np.outer(output_gradients, hidden_outputs)
    weights_input_hidden += learning_rate * np.outer(hidden_gradients, inputs)

def train_xor_network(inputs, targets, hidden_size, epochs, learning_rate):
    input_size = len(inputs[0])
    output_size = len(targets[0])

    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

    for epoch in range(epochs):
        for i in range(len(inputs)):
            input_data = inputs[i]
            target_data = targets[i]

            hidden_outputs, final_outputs = forward_propagation(input_data, weights_input_hidden, weights_hidden_output)

            output_gradients, hidden_gradients = backward_propagation(input_data, target_data, hidden_outputs, final_outputs, weights_hidden_output)

            update_weights(input_data, hidden_outputs, output_gradients, hidden_gradients,
                           weights_input_hidden, weights_hidden_output, learning_rate)

        if epoch % 1000 == 0:
            error = 0.5 * np.sum((targets - forward_propagation(inputs, weights_input_hidden, weights_hidden_output)[1]) ** 2)
            print(f"Epoch: {epoch}, Error: {error}")

    return weights_input_hidden, weights_hidden_output

def test_xor_network(inputs, weights_input_hidden, weights_hidden_output):
    for i in range(len(inputs)):
        input_data = inputs[i] 
        _, output = forward_propagation(input_data, weights_input_hidden, weights_hidden_output)
        print(f"Input: {input_data}, Output: {output}")

if _name_ == "_main_":
    # XOR function inputs and corresponding bipolar outputs
    xor_inputs = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    xor_targets = np.array([[1], [-1], [-1], [1]])

    hidden_layer_size = 2
    training_epochs = 10000
    learning_rate = 0.1

    trained_weights_input_hidden, trained_weights_hidden_output = train_xor_network(
        xor_inputs, xor_targets, hidden_layer_size, training_epochs, learning_rate)

    print("\nTrained XOR Network:")
    test_xor_network(xor_inputs, trained_weights_input_hidden, trained_weights_hidden_output)



''')

    def h1(self):
        print('''
    # program1 
1.Analyze the “phone” dataset and answer the following questions using R:  
i.Find the number of Vodafone users 
ii.Find the number of call whose duration is greater than 15 mins 
iii.Find the month of top 5 duration calls 
iv.Find the average duration of each network type. 
v.Find the average duration of each item for each network 
vi.Find the count of each item for each network 
vii.Find which month contains a greater number of calls 
viii.Find total number of messages sent by world users 
ix.Find the proportion of Meteor user is the network 
x.Check which month has the highest duration with appropriate methods.

# Load the necessary library
library(dplyr)

# Read the dataset
phone_data <- read.csv("phone_data.csv")

phone_data

install.packages('IRkernel')
IRkernel::installspec(name = 'ir35', displayname = 'R 3.6.3')

# i. Find the number of Vodafone users 
vodafone_users <- phone_data %>%
    filter(network == "Vodafone") %>% 
    nrow() 

vodafone_users

# ii. Find the number of calls whose duration is greater than 15 minutes in the 'ph 
number_of_calls <- sum(phone_data$duration > 15)

# Print the number of calls 
number_of_calls

#iii.Find the month of top 5 duration calls 
top5_duration_calls <- phone_data %>%  filter(item == "call") %>%  
arrange(desc(duration)) %>%  distinct(month, .keep_all = TRUE) %>%  
head(5)

# Print the top 5 months with their corresponding durations 
print(top5_duration_calls)

# iv. Find the average duration of each network type 
avg_duration_by_network_type <- phone_data %>%  
  group_by(network_type) %>% 
  summarise(avg_duration = mean(duration)) 

avg_duration_by_network_type

# v. Find the average duration of each item for each network
avg_duration_by_item_network <- phone_data %>% 
  group_by(item, network) %>% 
  summarise(avg_duration = mean(duration))

avg_duration_by_item_network

# vi. Find the count of each item for each network
count_by_item_network <- phone_data %>%  
  group_by(item, network) %>%   
  summarise(count = n())  

count_by_item_network

# viii. Find the total number of messages sent by world users 
total_messages_world_users <- phone_data %>%  
  filter(network == "world" & item == "sms") %>%  
  nrow()

total_messages_world_users 

# ix. Find the proportion of Meteor users in the network 
proportion_meteor_users <- phone_data %>% 
  filter(network == "Meteor") %>%  
  nrow() / nrow(phone_data) 

proportion_meteor_users

# x. Check which month has the highest duration
month_with_highest_duration <- phone_data %>% 
  group_by(month) %>%  
  summarise(total_duration = sum(duration)) %>%  
  arrange(desc(total_duration)) %>%  
  head(1) 

month_with_highest_duration
''')
    def h2(self):
        print('''
#2.Analyze the “mpg” dataset and answer the following questions using R:  
i.Visualize the distribution of city mpg 
ii.Show the counts of each car type 
iii.Visualize the relationship between displacement and highway mpg
iv.Display the distribution of engine cylinder counts
v.Subset the dataset to include cars manufactured by Toyota. 
vi.Find cars with a city mpg greater than 20 and highway mpg greater than 30. 
vii.Create a new column "mileage_difference" as the difference between city mpg and 
viii.Calculate the average city mpg for each car class and sort them in descending
ix.Find the mean highway mpg for cars manufactured in the United States. 
x.Group the data by transmission type and calculate the median engine displacement. 
xi.Investigate if there is a trend between model year and city mpg 
xii.Detect and list the cars with exceptionally high highway mpg values (potential  

install.packages("ggplot2") 
library(ggplot2)

data(mpg)

mpg


Here are the key variables (columns) in the "mpg" dataset:
manufacturer: The manufacturer or brand of the car.
model: The model name of the car. 
displ: The engine displacement in liters. 
year: The manufacturing year of the car.
cyl: The number of cylinders in the engine.
trans: The type of transmission (e.g., automatic or manual) and the number of gears
drv: The type of drive system (e.g., 4-wheel drive or front-wheel drive). 
cty: The city miles per gallon (mpg) rating. 
hwy: The highway miles per gallon (mpg) rating. 
fl: The fuel type (e.g., regular, premium, or diesel). class: The vehicle class (e.g., compact, midsize, or suv).

#i. Visualize the distribution of city mpg 
# Histogram of City MPG
hist(mpg$cty, main = "Distribution of City MPG", xlab = "City MPG")

#ii. Show the counts of each car type: 
# Bar Plot of Car Types 
barplot(table(mpg$class), main = "Counts of Each Car Type", xlab = "Car Type")

#iii. Visualize the relationship between displacement and highway mpg:  
# Scatter Plot of Displacement vs. Highway MPG 
plot(mpg$displ, mpg$hwy, main = "Displacement vs. Highway MPG", xlab = "Displacement", ylab = "Highway MPG"

#iv. Display the distribution of engine cylinder counts: 
# Box Plot of Cylinder Counts 
boxplot(mpg$cyl, main = "Distribution of Engine Cylinder Counts", ylab = "Cylinder"

#v. Subset the dataset to include cars manufactured by Toyota:
# Subset for Toyota Cars 
toyota_cars <- subset(mpg, manufacturer == "toyota") 
toyota_cars

#vi. Find cars with a city mpg greater than 20 and highway mpg greater than 30:
# Subset for High Mileage Cars 
high_mileage_cars <- subset(mpg, cty > 20 & hwy > 30)
high_mileage_cars

#vii. Create a new column "mileage_difference" as the difference between city mpg a 
# Create Mileage Difference Column 
mpg$mileage_difference <- mpg$cty - mpg$hwy 
mpg$mileage_difference

#viii. Calculate the average city mpg for each car class and sort them in descendin
# Average City MPG by Car Class
avg_city_mpg <- aggregate(cty ~ class, data = mpg, FUN = mean) 
avg_city_mpg_sorted <- avg_city_mpg[order(avg_city_mpg$cty, decreasing = TRUE), ] 
avg_city_mpg_sorted

#ix. Group the data by transmission type and calculate the median engine displaceme 
# Median Displacement by Transmission Type
median_displacement <- aggregate(displ ~ trans, data = mpg, FUN = median) 
median_displacement

#x. Investigate if there is a trend between model year and city mpg: 
# Scatter Plot of Model Year vs. City MPG 
plot(mpg$year, mpg$cty, main = "Model Year vs. City MPG", xlab = "Model Year", ylab

#xi. Detect and list the cars with exceptionally high highway mpg values (potential  
# Identify Outliers (e.g., highway mpg > 40) 
outliers <- subset(mpg, hwy > 40)
outliers

''')
    def h3(self):
        print('''
# 3.Analyze the “airlines” dataset and answer the following questions using R:
i.Find the descriptive statistics of all the columns. Write the inference 
ii.Plot the distribution of all the numerical columns(univariate). Infer the result
iii.Plot the counts of all the categorical columns(univariate). Infer the results. 
iv.Find top 5 airlines where the maximum delay happened. Plot it with appropriate g
v.Plot the distribution of time of delay and no delay(bivariate). Write the inferen 
vi.Plot the distribution of length of delay and no delay(bivariate. Write the infer 
vii. Determine the distribution of flight counts for each airport of arrival (Airpo

airlines <- read.csv("airlines.csv")

airlines

#i Find descriptive statistics for all columns 
summary(airlines)

#ii. Plot the distribution of numerical columns 
# Specify numerical columns 
numerical_columns <- c("Flight", "DayOfWeek", "Time", "Length", "Delay") 
# Create histograms 
for each numerical column for (column in numerical_columns) {  
# Create a histogram with density plot (kde)  
hist_data <- airlines[[column]] 
hist_density <- density(hist_data)   
# Plot the histogram  
hist_obj <- hist(hist_data, main = paste("Distribution of", column), xlab = colum   
# Add a density plot (kde) 
lines(hist_density, col = "blue", lwd = 2)    
# Add labels
xlabel <- paste(column, "(Value)") 
ylabel <- "Frequency"  
title <- paste("Distribution of", column)  
legend("topright", legend = "KDE", col = "blue", lwd = 2)  
# Customize labels and titles  
xlabel <- paste(column, "(Value)") 
ylabel <- "Frequency"
title <- paste("Distribution of", column)    
# Add labels and title  
xlabel <- paste(column, "(Value)")  
ylabel <- "Frequency" 
title <- paste("Distribution of", column)  
title(main = title, xlab = xlabel, ylab = ylabel)
} 

#iii. Plot the distribution of numerical columns 
# Load the ggplot2 library 
library(ggplot2)
# Define your categorical columns
categorical_columns <- c("Airline", "AirportFrom", "AirportTo")
# Loop through each categorical column 
for (column in categorical_columns) { 
# Create a ggplot object  
    plot <- ggplot(data = airlines, aes_string(x = column)) +    geom_bar() +  
    # Create a bar plot 
    labs(x = column, y = "Count", title = paste("Counts of", column)) +   
    theme(axis.text.x = element_text(angle = 90, hjust = 1))  # Rotate x-axis label      
# Print the plot 
    print(plot) 
} 

# iv. Find and plot the top 5 airlines with maximum delay 
library(dplyr)
library(ggplot2) 
# Assuming your dataset is named 'df' 
# Group by 'Airline' and calculate the sum of 'Delay', then arrange in descending o
top_airlines <- airlines %>% 
group_by(Airline) %>%  
summarize(Delay = sum(Delay)) %>%  
arrange(desc(Delay)) %>%  
head(5)
# Create a bar plot 
ggplot(top_airlines, aes(x = reorder(Airline, -Delay), y = Delay)) +
  geom_bar(stat = "identity", fill = "blue") + 
  labs(x = "Airline", y = "Delay", title = "Top 5 Airlines with Maximum Delay") + 
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  
  coord_flip()  # To make the bars horizontal

# v. Plot the distribution of time of delay and no delay(bivariate). Write the infe 
# Create a new column 'Delay_Status' with values "Delay" or "No Delay" 
airlines$Delay_Status <- ifelse(airlines$Delay == 1, "Delay", "No Delay")
# Load the ggplot2 package if not already loaded 
library(ggplot2)
# Create a boxplot
ggplot(airlines, aes(x = Delay_Status, y = Time)) + 
  geom_boxplot() +
  labs(x = "Delay Status", y = "Time", title = "Distribution of Time for Delay and 

#vi.Plot the distribution of length of delay and no delay(bivariate) 
# Load the ggplot2 package if not already loaded
library(ggplot2)
# Create a boxplot
ggplot(airlines, aes(x = as.factor(Delay), y = Length)) +
  geom_boxplot() + 
  labs(x = "Delay", y = "Length", title = "Distribution of Length for Delay and No 

#vii. Determine the distribution of flight counts for each airport of arrival (Airp 
# Load the necessary libraries
library(dplyr)
library(ggplot2)  


# Group the data by AirportTo and calculate the flight counts 
flight_counts <- airlines %>%  
  group_by(AirportTo) %>%  
  summarise(Flight_Count = n())

# Create a bar plot to visualize the distribution of flight counts 
ggplot(flight_counts, aes(x = reorder(AirportTo, -Flight_Count), y = Flight_Count))  
  geom_bar(stat = "identity", fill = "lightblue", color = "black") +  
  labs(title = "Distribution of Flight Counts by Airport of Arrival", x = "Airport  
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
  ggsave("Flight_Counts_by_AirportTo.png")
''')
    def h4(self):
        print('''
              
#4.Analyze the “economics” dataset and answer the following questions using R:
i.Calculate the average unemployment rate over the entire time period. 
ii.Calculate the quarterly percentage changes in the Gross Domestic Product (GDP) a identify the quarter with the highest and lowest change. 
iii.Calculate the average inflation rate (percentage change in the Consumer Price I 
iv.Visualize the unemployment rate trends over time. 
v.Examine the relationship between inflation and unemployment. 
vi.Visualize the average unemployment rate for each year.
vii.Compare the growth rates of GDP and personal consumption.
viii.Visualize the fluctuations in the inflation rate.
ix.Compare the trends of GDP, personal consumption, and the unemployment rate.

library(ggplot2) 

# Load the economics dataset 
data("economics")

economics

# i. Average Unemployment Rate 
avg_unemployment_rate <- mean(economics$unemploy)
avg_unemployment_rate

# ii. Quarterly GDP Changes
library(lubridate)
library(dplyr) 
quarterly_changes <- economics %>%  
  mutate(year_quarter = paste(year(date), "Q", quarter(date), sep="")) %>%  
  group_by(year_quarter) %>%  
  summarise(quarterly_change = (max(pce) - min(pce)) / min(pce) * 100) 

max_change <- quarterly_changes[which.max(quarterly_changes$quarterly_change), ] 
min_change <- quarterly_changes[which.min(quarterly_changes$quarterly_change), ]

min_change 
max_change

# iii. Inflation Analysis 
avg_inflation_rate <- mean(economics$psavert) 
avg_inflation_rate

# iv. Unemployment Trends 
unemployment_trends_plot <- ggplot(data=economics, aes(x=date, y=unemploy)) + 
  geom_line() +  
  labs(x="Date", y="Unemployment Rate") +  
  ggtitle("Unemployment Rate Trends Over Time")

unemployment_trends_plot

# v. Inflation vs. Unemployment 
inflation_unemployment_plot <- ggplot(data=economics, aes(x=psavert, y=unemploy)) + 
  geom_point() +  
  labs(x="Personal Savings Rate", y="Unemployment Rate") +  
  ggtitle("Relationship Between Personal Savings Rate and Unemployment Rate")

inflation_unemployment_plot

# vi. Unemployment Rate by Year 
unemployment_by_year_plot <- ggplot(data=economics, aes(x=year(date), y=unemploy))   
  geom_bar(stat="summary", fun=mean) +  
  labs(x="Year", y="Average Unemployment Rate") + 
  ggtitle("Average Unemployment Rate by Year") 
unemployment_by_year_plot

# vii. GDP and Personal Consumption Comparison
gdp_personal_consumption_comparison_plot <- ggplot(data=economics, aes(x=year(date)  
  geom_bar(stat="summary", aes(y=pce, fill="Personal Consumption"), alpha=0.6) +  
  geom_bar(stat="summary", aes(y=pop, fill="GDP"), alpha=0.6) +  
  labs(x="Year", y="Value") +  
  scale_fill_manual(values=c("Personal Consumption"="blue", "GDP"="green")) +  
  ggtitle("Comparison of Personal Consumption and GDP by Year")
                                                                       
gdp_personal_consumption_comparison_plot

# viii. Inflation Rate Fluctuations
inflation_fluctuations_plot <- ggplot(data=economics, aes(x=date, y=psavert)) + 
  geom_point() +  
  labs(x="Date", y="Personal Savings Rate") + 
  ggtitle("Personal Savings Rate Fluctuations")

inflation_fluctuations_plot

# ix. Economic Indicators Comparison
economic_indicators_comparison_plot <- ggplot(data=economics, aes(x=date)) + 
  geom_line(aes(y=pce, color="Personal Consumption"), alpha=0.6) +  
  geom_line(aes(y=pop, color="GDP"), alpha=0.6) + 
  labs(x="Date", y="Value") + 
  scale_color_manual(values=c("Personal Consumption"="blue", "GDP"="green")) +  
  ggtitle("Comparison of Economic Indicators Over Time") 

economic_indicators_comparison_plot
''')

   