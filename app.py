import streamlit as st
import random

# Sample Pokémon data (you can extend or pull from PokéAPI)
POKEMON_DATA = {
    "fire": ["Charmander", "Vulpix", "Growlithe"],
    "water": ["Squirtle", "Psyduck", "Totodile"],
    "grass": ["Bulbasaur", "Chikorita", "Oddish"],
    "electric": ["Pikachu", "Electabuzz", "Mareep"],
    "psychic": ["Abra", "Espeon", "Ralts"]
}

# Simulated investment returns
def simulate_investment(pokemon_name):
    base_value = random.randint(100, 1000)
    multiplier = round(random.uniform(1.1, 3.5), 2)
    return base_value, round(base_value * multiplier, 2)

# Sidebar: user input
st.sidebar.title("Poke Ventures")
username = st.sidebar.text_input("Your Name")
poke_type = st.sidebar.selectbox("Select Pokémon Type", list(POKEMON_DATA.keys()))

# Main section
st.title("🚀 Welcome to Poke Ventures!")

if username:
    st.subheader(f"Hello {username}, let's explore your Pokémon investment journey!")
    st.write(f"✨ You've selected the **{poke_type.capitalize()}** type Pokémon.")

    # Random Pokémon from type
    chosen_pokemon = random.choice(POKEMON_DATA[poke_type])
    st.image(f"https://img.pokemondb.net/artwork/large/{chosen_pokemon.lower()}.jpg", width=200)
    st.success(f"You've discovered: **{chosen_pokemon}**!")

    # Simulated investment
    st.markdown("### 💸 Investment Simulator")
    if st.button("Simulate Investment"):
        cost, return_val = simulate_investment(chosen_pokemon)
        st.write(f"Initial Investment in **{chosen_pokemon}**: ${cost}")
        st.write(f"Your Return: ${return_val}")
        st.balloons()

else:
    st.info("👈 Please enter your name and choose a Pokémon type to begin.")

