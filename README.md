# StayEasy

![StayEasy Logo](https://via.placeholder.com/150)

**StayEasy** is a website designed to simplify and enhance the process of finding, booking, and managing accommodations. Whether you're a traveler seeking a cozy place to stay or a host looking to list your property, StayEasy offers an intuitive and secure platform inspired by the functionality of Airbnb.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [🚀 Getting Started](#getting-started)
  - [🔧 Prerequisites](#prerequisites)
  - [📂 Installation](#installation)
- [💻 Usage](#usage)
- [✨ Features](#features)
- [👥 Contributors](#contributors)
- [🙌 Acknowledgments](#acknowledgments)

---

## 🏗 About The Project

StayEasy is your go-to solution for seamless accommodation booking. Designed with user-friendliness in mind, our website bridges the gap between hosts and guests, ensuring an efficient and enjoyable experience for both.

**Key Objectives:**
- Provide a modern platform for listing and discovering accommodations.
- Ensure secure transactions between hosts and guests.
- Offer additional features like reviews, availability management, and location-based searches.

---

### 🛠 Built With

This project is built using the following technologies:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **: Backend functionality.**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) **: Frontend structure and styling.**
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) **: Framework for web development.**
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) **: Database for managing user data, property listings, and transactions.**
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) **: Responsive and mobile-first design.**

[Back to top](#stayeasy)

---

## 🚀 Getting Started

To set up and run the StayEasy project locally, follow these steps:

### 🔧 Prerequisites

Before you start, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads/) - Programming language for backend development.
- [Git](https://git-scm.com/downloads) - Version control system.
- A virtual environment tool such as venv or virtualenv.

---

### 📂 Installation

1. **Clone the Repository**:  
   Open your terminal and run the following commands:
   ```bash
   git clone https://github.com/Boyax123123/IM2-Proj-StayEasy.git
   cd IM2-Proj-StayEasy
2. Set Up a Virtual Environment:
Create and activate a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate
3. Install Dependencies:
Install the required Python packages listed in requirements.txt:
   ```bash
   pip install -r requirements.txt
4. Set Up the Database:
Migrate the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. Run the Application:
   Start the development server:
   ```bash
   python manage.py runserver

## 💻 Usage

### 👤 Guests
- 🏡 **Browse accommodations** by location, price, or amenities.
- 🔒 **Book accommodations securely** and leave reviews for hosts.

### 🏠 Hosts
- 📸 **List properties** with photos, descriptions, and pricing details.
- 📅 **Manage bookings** and interact with guests.

### 🛡️ Admin
- 🔍 **Oversee platform activity** and manage disputes between users.

---

## ✨ Features

### 1. 🛂 **User Registration and Login**
- **Requirement**: Users can register and log in securely.
- **Rationale**: Allows users to create accounts, access personal information, and manage bookings.
- **MVP Implementation**:
  - User registration form with fields like name, email, and password.
  - Email verification for new users.
  - Secure login functionality using password hashing and salting.
  - Basic user profile management (edit name, email, etc.).

---

### 2. ⭐ **Review and Rating System**
- **Requirement**: Guests can leave reviews and ratings for hosts and properties.
- **Rationale**: Builds trust and credibility, enabling guests to make informed booking decisions.
- **MVP Implementation**:
  - Review form with a rating system (e.g., 1-5 stars).
  - Moderation system to ensure accuracy and fairness.
  - Host response feature to allow hosts to reply to reviews.
  - Display reviews and ratings on property detail pages.

---

### 3. 🔍 **Search and Booking**
- **Requirement**: Guests can search for properties based on location, dates, and amenities.
- **Rationale**: Core functionality for finding and booking accommodations.
- **MVP Implementation**:
  - Search function with basic filters (e.g., location, dates, price range).
  - Property detail pages with descriptions, photos, and amenities.
  - Booking calendar to display availability.

---

### 4. 💾 **Wishlist**
- **Requirement**: Guests can save properties to a wishlist for future reference.
- **Rationale**: Enables guests to easily track and revisit their favorite properties.
- **MVP Implementation**:
  - Wishlist button on property detail pages.
  - Guest wishlist page displaying saved properties.
  - Option to remove properties from the wishlist.

---

### 5. 💳 **Payment Processing**
- **Requirement**: Securely process payments for bookings using multiple payment methods.
- **Rationale**: Ensures smooth financial transactions between guests and hosts.
- **MVP Implementation**:
  - Integration with reputable payment gateways like GCash.
  - Support for payment methods such as credit cards, bank transfers, e-wallets, and cash.
  - Payment confirmation and receipt generation.

---

### 6. 📅 **Booking Confirmation and Management**
- **Requirement**: Generate booking confirmations and provide hosts with tools to manage bookings.
- **Rationale**: Ensures clear communication and efficient booking management.
- **MVP Implementation**:
  - Automated booking confirmation emails to guests.
  - Host dashboard to view upcoming and past bookings.
  - Booking management features like updating booking status and viewing guest details.

---
## 👥 Contributors

Thanks to these amazing collaborators for their contributions to the project:

<div style="display: flex; flex-direction: column; align-items: center; gap: 30px; margin-top: 20px;">

<div style="text-align: center; margin-bottom: 20px;">
  <a href="https://github.com/Boyax123123">
    <img src="https://github.com/Boyax123123.png?size=100" width="80" height="80" style="border-radius: 50%;" alt="Boyax123123" />
  </a>
  <br />
  <a href="https://github.com/Boyax123123" style="text-decoration: none; color: black;">
    <strong>Boyax123123</strong>
  </a>
</div>

<div style="text-align: center; margin-bottom: 20px;">
  <a href="https://github.com/darkn38">
    <img src="https://github.com/darkn38.png?size=100" width="80" height="80" style="border-radius: 50%;" alt="darkn38" />
  </a>
  <br />
  <a href="https://github.com/darkn38" style="text-decoration: none; color: black;">
    <strong>darkn38</strong>
  </a>
</div>

<div style="text-align: center; margin-bottom: 20px;">
  <a href="https://github.com/Contributor3">
    <img src="https://via.placeholder.com/100" width="80" height="80" style="border-radius: 50%;" alt="Contributor 3" />
  </a>
  <br />
  <a href="https://github.com/Contributor3" style="text-decoration: none; color: black;">
    <strong>Contributor 3</strong>
  </a>
</div>

</div>

---

## 🙌 Acknowledgments

We would like to thank the following resources and individuals for their inspiration, guidance, and contributions to this project:

---

### ![Airbnb](https://img.shields.io/badge/Airbnb-FF5A5F?style=for-the-badge&logo=airbnb&logoColor=white)  
For inspiring the concept and features of StayEasy.  
**[Visit Airbnb](https://www.airbnb.com)**

---

### ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)  
For providing responsive and mobile-first design elements.  
**[Visit Bootstrap](https://getbootstrap.com)**

---

### ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)  
For their detailed framework guides and community support.  
**[Visit Django Documentation](https://docs.djangoproject.com)**

---

### ![Unsplash](https://img.shields.io/badge/Unsplash-000000?style=for-the-badge&logo=unsplash&logoColor=white)  
For free, high-quality images used in our project.  
**[Visit Unsplash](https://unsplash.com)**

---

### ![Shields.io](https://img.shields.io/badge/Shields.io-555555?style=for-the-badge&logo=shieldsdotio&logoColor=white)  
For creating beautiful and customizable badges for this README.  
**[Visit Shields.io](https://shields.io)**

---

### ![All Contributors](https://img.shields.io/badge/All%20Contributors-FE7D37?style=for-the-badge&logo=allcontributors&logoColor=white)  
For making it easy to recognize project collaborators.  
**[Visit All Contributors](https://allcontributors.org/)**

---

### Our Amazing Team Members:
- [Boyax123123](https://github.com/Boyax123123)  
- [darkn38](https://github.com/darkn38)  
- [Contributor 3](https://github.com/Contributor3)

---

Your support and resources helped make StayEasy a success. 🙏

[Back to top](#stayeasy)

