##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
This project is a web scraping script that fetches the list of the top 100 movies from a specific archived webpage and saves it into a CSV file. The project uses the requests library to retrieve the webpage, BeautifulSoup to parse the HTML content, and pandas to store the data and export it to a CSV file.

## 📝 How to Build
**Prerequisites**
  - Requests
  - beautifulsoup4
  - Pandas

 **To build the project follow these steps:**
   - **Installation:**
  ```shell
  # Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)
  
  # Ensure Git is installed
  # Visit https://git-scm.com to download and install console Git if not already installed
              
  # Clone the repository
  git clone https://github.com/Akwaowo91/Movies-to-watch.git
  cd Movies-to-watch       
  
  # Install the required package
  pip install pandas
  pip install beautifulsoup4
  ```
  - **Documentation:**
      - Beautiful Soup: https://beautiful-soup-4.readthedocs.io/en/latest/
      - Pandas: https://pandas.pydata.org/docs/

## 📄 Code Explanation
  - The script performs the following steps:
      - Send a GET request to the specified URL of the archived webpage.
      - Parse the HTML content using BeautifulSoup.
      - Extract the movie titles from the webpage.
      - Reverse the list to ensure the movies are ordered from 1 to 100.
      - Save the list of movies to a CSV file named movies_to_watch.csv.
   
- **Check the output:**
  - After running the script, you will find the movies_to_watch.csv file in the project directory. This file will contain the list of top 100 movies, with the numbering starting from 1.
 
## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Movies-to-watch project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Movies-to-watch project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
