import streamlit as st
import random

# Expanded Pokémon data (50 Pokémon across 10 types)
POKEMON_DATA = {
    "fire": ["Charmander", "Vulpix", "Growlithe", "Cyndaquil", "Torchic"],
    "water": ["Squirtle", "Psyduck", "Totodile", "Mudkip", "Piplup"],
    "grass": ["Bulbasaur", "Chikorita", "Oddish", "Treecko", "Turtwig"],
    "electric": ["Pikachu", "Electabuzz", "Mareep", "Shinx", "Jolteon"],
    "psychic": ["Abra", "Espeon", "Ralts", "Gothita", "Solosis"],
    "dragon": ["Dratini", "Bagon", "Gible", "Axew", "Noibat"],
    "dark": ["Murkrow", "Houndour", "Poochyena", "Zorua", "Nickit"],
    "fairy": ["Clefairy", "Jigglypuff", "Togepi", "Snubbull", "Sylveon"],
    "fighting": ["Machop", "Tyrogue", "Riolu", "Mankey", "Hitmonlee"],
    "ice": ["Snover", "Snorunt", "Swinub", "Spheal", "Vanillite"]
}

# Simulate investment return
def simulate_investment(pokemon_name):
    base = random.randint(50, 1000)
    multiplier = round(random.uniform(1.2, 4.5), 2)
    return base, round(base * multiplier, 2)

# --- Sidebar ---
st.sidebar.title("🎒 Poke Verse Ventures")
username = st.sidebar.text_input("Trainer Name", placeholder="e.g., Ash, Misty")
poke_type = st.sidebar.selectbox("Pick Your Pokémon Type", sorted(POKEMON_DATA.keys()))
st.sidebar.markdown("---")
st.sidebar.info("🔴 Follow us live on **Whatnot** for Pokémon pack breaks, giveaways, and exclusive auctions!")

# --- Header & Intro ---
st.title("🌟 Poke Verse Ventures")
st.markdown("""
## 🧢 Your Adventure Starts Here!

At **Poke Verse Ventures**, we turn Pokémon collecting into a live experience.  
Join us on **Whatnot** for:

- 🔥 **Live pack breaks** with chase pulls
- 🎁 **Slab auctions**, sealed bundles, and mystery packs
- 💬 Collector Q&As, giveaways, and market tips

Whether you're after nostalgia or the next grail card, we’ve got something for every trainer.
""")

# --- Main Experience ---
if username:
    st.subheader(f"👋 Welcome, Trainer {username}!")
    st.write(f"You're exploring the world of **{poke_type.capitalize()}**-type Pokémon.")

    # Choose random Pokémon
    chosen_pokemon = random.choice(POKEMON_DATA[poke_type])
    image_url = f"https://img.pokemondb.net/artwork/large/{chosen_pokemon.lower()}.jpg"

    st.image(image_url, caption=f"You discovered: **{chosen_pokemon}**", width=300)

    # Investment simulation
    st.markdown("### 💸 Investment Simulator")
    if st.button("Simulate Pokémon Investment"):
        cost, value = simulate_investment(chosen_pokemon)
        st.success(f"You invested ${cost} in {chosen_pokemon}. Current value: ${value}")
        st.balloons()

    # Live sales preview section
    st.markdown("### 📦 Upcoming Live Whatnot Sales")
    st.info("""
    🗓️ **Next Show:** Friday at 8PM EST  
    🧵 Featuring: Graded slabs, 90s era holos, and modern hits  
    🎉 Giveaways every 15 minutes — don’t miss out!
    """)
else:
    st.warning("Enter your Trainer Name in the sidebar to begin your journey.")

# --- Footer ---
st.markdown("---")
st.markdown("""
📍 [Visit Us on Whatnot](https://www.whatnot.com/)  
📧 Contact: pokeverseventures@example.com  
© 2025 Poke Verse Ventures. Gotta buy 'em all!
""")


