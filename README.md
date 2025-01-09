# Pokemon Project

## Overview
This project is a web application built using Django that allows users to search for information about their favorite Pokémon. It leverages a Pokémon API to extract details like typing and movesets, and it also displays an animated GIF of the searched Pokémon. Users have the option to view shiny variants of the Pokémon as well.

## Features
- **Search for Pokémon:** Enter the name of a Pokémon to fetch its details.
- **Typing and Movesets:** Display the Pokémon's type(s) and its moveset.
- **Animated GIFs:** View an animated GIF of the searched Pokémon.
- **Shiny Mode:** Option to view the shiny version of the Pokémon.

## Technologies Used
- **Backend Framework:** Django
- **API Integration:** Pokémon API
- **Frontend:** HTML, CSS
- **Additional Media:** Animated Pokémon GIFs

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/pokemon-django-app.git
   cd pokemon-django-app
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Project:**
   - Create a `.env` file (if required) to store API keys or other configurations.

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage
- Enter the name of a Pokémon in the search bar.
- View its type(s), moveset, and an animated GIF.
- Toggle the shiny mode to view the shiny version of the Pokémon.

## API Reference
This application uses the Pokémon API to fetch Pokémon data. Learn more about the API [here](https://pokeapi.co/).

## Future Enhancements
- Add a search history feature.
- Enable comparison between multiple Pokémon.
- Add support for different languages.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Special thanks to [PokéAPI](https://pokeapi.co/) for providing a comprehensive Pokémon database.
- Thanks to the contributors and the open-source community.

---

Enjoy exploring the world of Pokémon!

