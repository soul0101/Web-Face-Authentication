
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
![Project-Title](https://fontmeme.com/permalink/210324/609738aab7b1c03de1e7223bccaccf76.png)

* [Heroku Deployment](https://face-login0101.herokuapp.com)

This projects demonstrates a scenario where a user can login to a system using his Face. The user has to capture their face during the signup using a web-camera or 
the inbuilt camera of their mobile phones from whcih the facial landmarks will be extracted and stored on the data base. <br>
During signup the use has the option of logging in with their <b>Face</b> or with the <b>Password</b>. If the user wishes to login with their face, they have to enter their 
username and snap a picture of their face upon which the system grants access based on the matching of the Facial Features.

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [JavaScript](https://www.javascript.com/)
* [face-recognition](https://github.com/ageitgey/face_recognition)




<!-- GETTING STARTED -->
## Getting Started

This project uses the face-recognition library which is built upon dlib a C++ toolkit.<br>
To avoid hassle free installation I would suggest you to use Anaconda and create a virtual environment.

### Prerequisites
Anaconda installed on your system if running locally.
### Installation


1. Create a Conda Virtual Environment
   ```sh
   conda create -n yourenvname
   ```
2. Activate the Virtual Environment
   ```sh
   conda activate yourenvname
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/soul0101/Web-Face-Authentication.git
   ```
3. Install the packages in requirements.txt
   ```sh
   pip install -r requirements.txt
   ```




<!-- ROADMAP -->
## Roadmap
Additional work to be done:

1. Beautification of the webpages.
2. Improving mobile compatibility.
3. Increasing accuracy of face-recognition by taking multipe images at registration.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Contact- chirag.hegde01@gmail.com

Project Link: [https://github.com/soul0101/Web-Face-Authentication](https://github.com/soul0101/Web-Face-Authentication)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Django x Docker Integration to Heroku](https://www.codingforentrepreneurs.com/blog/django-docker-production-heroku/)
* [Dockerfile Example](https://github.com/ageitgey/face_recognition/blob/master/Dockerfile)
* [Project Title Image](https://fontmeme.com/pixel-fonts/)

 
