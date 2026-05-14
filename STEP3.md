# Step 3 – Testing, Deployment Preparation, and Data Handling

## 1. Description of the Testing Process

A manual testing process was conducted with the AI Personal Assistant Agent that is built using a command-line interface (CLI) environment. The intent of the test was to check the accuracy of the language processing that could be done by the system, to check correctness of the identification of the tool to use, to check if the system can select the right tool, to check if the system can execute the selected tool and to check if the system can return a meaningful answer.

The testing process included multiple functional tests covering the main capabilities of the system. During testing, different user queries were entered to validate:

- General conversational interaction
- Time retrieval functionality
- Mathematical calculations
- Language translation
- File reading capability

The system was observed to ensure correct tool selection, accurate execution, proper response generation, and stable runtime behavior.

### Testing Evidence

The following screenshots demonstrate successful execution of different system functionalities:

- Greeting interaction (`Hello`)
- Time retrieval (`What time is it?`)
- Calculator functionality (`Calculate 25 * 8`)
- Translation functionality (`Translate "Good night" to French`)
- File reader functionality (`Read sample.txt`)

*(Insert screenshots here)*

---

## 2. List and Explanation of Test Scenarios

| Test Scenario | User Input | Expected Result | Actual Result |
|---------------|-------------|----------------|---------------|
| Greeting / Conversation | `Hello` | System responds naturally | Passed |
| Time Tool | `What time is it?` | Current local time returned | Passed |
| Calculator Tool | `Calculate 25 * 8` | Correct mathematical result | Passed |
| Translation Tool | `Translate "Good night" to French` | Correct translation generated | Passed |
| File Reader Tool | `Read sample.txt` | Contents of file displayed | Passed |

### Scenario Explanation

**Scenario 1 – Greeting Interaction**  
The purpose of this test was to verify whether the system could respond naturally to a normal user greeting without calling external tools.

**Scenario 2 – Time Retrieval**  
This test verified that the AI agent could identify a request related to time and correctly activate the Time Tool.

**Scenario 3 – Calculator Functionality**  
This scenario tested whether the system could detect a mathematical request and use the Calculator Tool to return an accurate answer.

**Scenario 4 – Translation Functionality**  
The Translation Tool was tested by requesting translation from English to French. The system successfully returned the translated phrase.

**Scenario 5 – File Reader Functionality**  
The File Reader Tool was tested by requesting the content of `sample.txt`. The system successfully accessed and displayed the file contents.

---

## 3. Deployment Preparation

The AI Personal Assistant Agent can be run locally on a computer with Python installed.

### Deployment Steps

1. Clone or download the project repository.
2. Open the project folder in a terminal.
3. Install required dependencies using:

```bash
pip install -r requirements.txt