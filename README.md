# Car Service/Maintenance Workshop Marketplace

This project aims to offer a marketplace for car maintenance workshops. The project allows car owners to search for 
workshops based on their location and the type of service they require. Workshop owners can register their businesses 
and add details about the services they offer.


## Features

- Multiple languages (English, Arabic).
- User registration, login, and logout.
- Fully customized user profile and password change.
- User activity log.
- Multiple cars for user.
- Search for workshops based on name, location, service type, brand and rate.
- Detailed workshop page (discounts, videos, locations, comments ..etc).
- Admin & staff can add details about their business, services, and pricing.
- Users can leave reviews - rate & comment - for workshops they have visited.
- User can report about workshop.
- Discounts & coupons are applied.
- Website main information (Social media links, mail, phone number, working hours).
- About us, Terms of use, FAQs, Privacy policy, Cookie policy, Contact us.
- Blog with ability of sharing opinions.


## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/mohamedgamalmoha/Car-Service-Marketplace.git
   ```
2. Install virtual environment package - outside project directory -, then activate it:
    ```shell
    pip install virtualenv
    virtualenv env 
    source env/bin/activate (Linux/Mac)
    env\Scripts\activate (Windows)
    ```
3. Navigate to project directory, then install the requirements of the project template by running:
    ```shell
    cd Car-Service-Marketplace
    pip install -r requirements.txt
    ```
4. Apply the migrations to create the database:
    ```shell
    python manage.py migrate
    ```
5. Check everything is being set up correctly:
    ```shell
    python manage.py check
    ```
6. Create a superuser account:
    ```shell
    python manage.py createsuperuser
    ```
7. Run server, then got the local [url](http://127.0.0.1:8000/):
    ```shell
    python manage.py runserver 
    ```

If you faced any problems setting up this project **please** feel free to inform us.


## Usage

### Multiple languages 
The website supports multiple languages. Currently English and Arabic are supported, but more languages in th future will be added.
User can change the language by clicking on the dropdown in the navigation bar and select the preferred language.

### User Registration/Login
Users can register by clicking on the "Register" link in the navigation bar. They will be asked to provide their username, email address, first & last name, 
password and password confirmation.\
Once registered, users can log in by clicking on the "Login" link in the navigation bar.

### User Profile
User can edit profile information. Could also change the account image, which displayed for others when he comments. 
User can view activity log for his actions. It is also possible to add more than one car.

### Workshop Adding/Editing
Workshops can be added or edited by the admin or staff at the dashboard. They will be asked to provide their business name, description, phone number, whatsapp, brands they are working with, 
services they offer, logo image, working hours, and multiple locations & videos . 

### Searching for Workshops
Users can search for workshops by clicking on the "Workshops" link in the navigation bar. They will be asked to select a service type from a dropdown menu and car brand. The option of sorting based on rate is also available.
The search results will display a list of workshops that match the user's criteria along with their address, phone number, andservices offered.

### Booking with workshop
After viewing the workshop detail page, and deciding it is the best choice. You could choose between the offers or 
simply book then the optimal discount will be applied in automatic way. There are some information needed, such as which car & service,  and serving time.  

### Leaving Reviews
Users who have visited a workshop can leave a review on workshop detail page. 
They will be asked to provide a rating (out of 5 stars) and write a comment about their experience.
The review will be displayed on the workshop's detail page along with its average rating based on all reviews received.
Also, users can report about workshop and upload attachment to support his claim.

### Blog
The admin write a post about specific topic, opening a field of discussion. Users can comment on those posts and share their opinions.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute code changes or suggest new features.

## License
This project is licensed under [Educational Use License](LICENSE).
