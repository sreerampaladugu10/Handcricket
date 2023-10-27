# Handcricket game project for the course: Foundations of Software Engineering - CPSC-8710
## link to play the game 
-https://sreerampaladugu10.github.io/Handcricket/

## Table of Contents
1. [Game Objective and Rules](#game-objective-and-rules)
2. [Technology Stack Used](#technology-stack-used)
3. [Setup and Deployment Instructions](#setup-and-deployment-instructions)
4. [Credits](#credits)
5. [Reflection](#reflection)

## Game Objective and Rules
- The Hand Cricket game is a simple yet fun game played between two players - a batsman and a bowler.
- Using their fingers, the batsman and bowler simultaneously show a number between 1 and 6.
- If the numbers get matched, then the batsman is out.
- If the numbers do not match, the batsman scores the number they showed.
- The objective is to outscore your opponent by predicting their moves and trying to stay in as the batsman for as long as possible.
- This process continues until both the batsman gets out and the player with the highest number of runs is the winner
- There is another mode in this game based on the number of players in the team. The player is asked to give input on the number of players going to play, and then the above process continues.

## Technology Stack Used
- **HTML**: For the game's user interface.
- **CSS**: For styling the game's interface.
- **JavaScript**: To handle the game logic and user interactions.
- **Python**: To implement the algorithm for guessing bumbers based on user input.
- **Bootstrap**: CSS Framework For designing the game's interface.

## Setup and Deployment Instructions
1. **Clone the Repository**: git clone https://github.com/sreerampaladugu10/Handcricket.git

2. **Open the Game**:
- Open the `index.html` file in your web browser to play the game.

3. **Play the Game**:
- Follow the on-screen instructions to play against the computer.

## Credits
- The game was developed by [Sreeram Paladugu,Akshatha arkit and Sairamakrishnak] and is open source.
- Special thanks to [bootstrap Framework] for their contributions to this project.
-picture credit background PNG Designed By Vector Illustration Canada from https://pngtree.com/freepng/cricket-player-illustration-vector-on-white-background_5293075.html?sol=downref&id=bef

## Reflection
In the process of designing and developing the Hand Cricket game, we encountered several challenges and learned valuable lessons:

- **Challenges Faced**:
- Developing a Hand Cricket game was a fun and rewarding project but can also come with challenges. Here are some common challenges we have faced while developing the Hand Cricket game:
- Game Logic: It can be challenging to make sure that the logic and rules of the game are applied correctly. There are specific rules for Hand Cricket; following them is crucial to a real gaming experience.
- It was difficult to simulate the hand cricket game experience digitally, as the game traditionally requires players to simultaneously show various hand gestures to indicate their chosen number. We were able to emulate this experience digitally in our game.

- **hurdles in implementing the Number guessing algorithm**:
 -The numbergueeser program is based on the Markov chain algorithm is a sequential model that uses the current state to predict the next state. It is based on the principle of memorylessness, which means that the next state only depends on the current state and not on the sequence of previous states.
 -If the numbers 1-6 were picked on random instead of using the Markov chain algorithm, the accuracy would be 16.67%. This is because there are 6 possible numbers that can be picked, and each number has an equal probability of being picked.
 -the markovs chain algorithm consistantly had a higher rate of accuracy compared to a random guesses from multiple tests.
 ![example of numberguesser program in action  ](<Screenshot 2023-10-27 at 3.02.29 PM.png>)
-Future work: We plan to implement a Markov chain algorithm in our game to predict user inputs based on their previous inputs. This will make the game more exciting and challenging for players.
 

- **What Worked**:
- Discussing the successful aspects of our design, development, and teamwork in the Hand Cricket game project
- User-Friendly Interface: One of the successful aspects of the project was the creation of a user-friendly and intuitive interface. The interface was designed to be visually appealing and easy to understand, making it accessible to players of all ages and skill levels.
- Effective Game Logic: The game's core logic, which involves predicting and countering the opponent's moves, was well-implemented. It created an engaging and competitive gaming experience, keeping players involved and challenged.
- Version Control: Utilizing Git and a version control system helped keep the project organized and allowed for easy tracking of changes. This was crucial in managing the codebase and collaborating with team members.
- Testing and bug fixing: Strict testing protocols and efficient bug-repair techniques were in place. In addition to improving the overall user experience, this guaranteed the game was reliable and devoid of serious bugs.
- effective coding techniques used : Our 'Reset/Restart Game' button offers a user-friendly experience by refreshing the page to start a new game, ensuring simplicity and compatibility across various browsers and devices.
- Algorithm Development: The development of the Python algorithm for simulating the opponent's moves was a significant achievement. It added an element of unpredictability to the game and made the single-player mode enjoyable and challenging.

- **What Didn't Work**:
- User Interface Issues: Although creating an intuitive user interface is crucial, things don't always go as to plan. The interface may not be straightforward or perplexing to users, which would make it less engaging.
- Balancing Difficulty Levels: It might be difficult to strike the correct balance between the bowler's and the batsman's chances of winning as the numbers are chosen randomly. The game could be very one-sided and less fun if the balance is off.
- mobile compatability Issues:The game is playable on mobile browsers, but it is best to play in landscape mode to avoid compatibility issues.

- **code or design decisions that must be revised.**:
- Game Logic Refinements: To ensure accuracy and fairness, the game logic, including the rules for innings, winning conditions, and scoring, may need to be updated. Finding areas that need improvement can be aided by regular testing and player input.
- User Interface Improvements: It could be necessary to make changes to the user interface (UI) to make it more intuitive and user-friendly. This can entail making the layout better, streamlining the navigation, or giving players useful tooltips or directions.
- Error Handling and Robustness: Code for error handling might need revision to provide better error messages and to prevent unexpected crashes. It's important to anticipate and handle various error scenarios.
- Performance Optimization: It could be required to make adjustments if the game runs slowly. This could entail employing performance-enhancing data structures or rewriting code to be more efficient.
 
- **Lessons Learned**:
- Rules Clarity is Crucial:It is critical to establish a precise and unambiguous set of guidelines. By ensuring that everyone is aware of the rules of the game, confusion and arguments are minimized.
- Balancing the Game: A big issue lies in balancing the game such that both the computer and the batsman are treated fairly. To attain this balance, it could be required to make adjustments to the scoring system and guidelines.
- Scoring System: Create a scoring system that recognizes and rewards accurate bowling and hitting. As a result, the game may become more competitive and interesting.
- Encourage Inclusivity: Make sure that your game is accessible and inclusive to players of all ages and skill levels.
- Testing and Feedback: Testing the game frequently with various player groups might aid in finding bugs and enhancing gameplay. Be receptive to criticism and ready to make the required adjustments.

-  **how these lessons can be applied to future projects**:
- Continuous Improvement: Make it a constant goal to optimize and improve your initiatives. Apply the lessons you've learned from the past to your upcoming endeavors.
- Record Keeping: Maintaining documentation of project progress, milestones, and data can facilitate performance analysis and enable data-driven decision-making for subsequent projects.
- Variation and Creativity: Encourage your teams to solve problems creatively. Motivate your team members to think creatively and unconventionally to solve problems.

The Hand Cricket game project was an enjoyable experience, and we look forward to further improvements and collaborations in the future. We hope you have as much fun playing the game as we did creating it!
