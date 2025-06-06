import streamlit as st
import random
import datetime
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Poke Verse Ventures CRM",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Pokémon data with rarity and market values
POKEMON_DATA = {
    "fire": {
        "common": ["Charmander", "Vulpix", "Growlithe", "Ponyta", "Magmar"],
        "rare": ["Cyndaquil", "Torchic", "Chimchar", "Tepig", "Fennekin"],
        "legendary": ["Moltres", "Entei", "Groudon", "Reshiram", "Volcanion"]
    },
    "water": {
        "common": ["Squirtle", "Psyduck", "Poliwag", "Tentacool", "Goldeen"],
        "rare": ["Totodile", "Mudkip", "Piplup", "Oshawott", "Froakie"],
        "legendary": ["Articuno", "Suicune", "Kyogre", "Palkia", "Manaphy"]
    },
    "grass": {
        "common": ["Bulbasaur", "Oddish", "Bellsprout", "Exeggcute", "Tangela"],
        "rare": ["Chikorita", "Treecko", "Turtwig", "Snivy", "Chespin"],
        "legendary": ["Celebi", "Virizion", "Shaymin", "Zarude", "Calyrex"]
    },
    "electric": {
        "common": ["Pikachu", "Voltorb", "Electabuzz", "Magnemite", "Jolteon"],
        "rare": ["Mareep", "Shinx", "Emolga", "Helioptile", "Togedemaru"],
        "legendary": ["Zapdos", "Raikou", "Thundurus", "Zekrom", "Zeraora"]
    },
    "psychic": {
        "common": ["Abra", "Drowzee", "Mr. Mime", "Jynx", "Espeon"],
        "rare": ["Ralts", "Gothita", "Solosis", "Inkay", "Hatenna"],
        "legendary": ["Mewtwo", "Mew", "Lugia", "Latios", "Deoxys"]
    },
    "dragon": {
        "common": ["Dratini", "Horsea", "Swablu", "Bagon", "Gible"],
        "rare": ["Axew", "Deino", "Goomy", "Jangmo-o", "Dreepy"],
        "legendary": ["Dragonite", "Rayquaza", "Dialga", "Giratina", "Eternatus"]
    },
    "dark": {
        "common": ["Murkrow", "Houndour", "Poochyena", "Sableye", "Absol"],
        "rare": ["Zorua", "Nickit", "Impidimp", "Morpeko", "Grimmsnarl"],
        "legendary": ["Darkrai", "Yveltal", "Guzzlord", "Urshifu", "Spectrier"]
    },
    "fairy": {
        "common": ["Clefairy", "Jigglypuff", "Togepi", "Snubbull", "Mawile"],
        "rare": ["Sylveon", "Dedenne", "Carbink", "Klefki", "Mimikyu"],
        "legendary": ["Xerneas", "Diancie", "Tapu Koko", "Zacian", "Zamazenta"]
    },
    "fighting": {
        "common": ["Machop", "Hitmonlee", "Tyrogue", "Makuhita", "Meditite"],
        "rare": ["Riolu", "Timburr", "Throh", "Sawk", "Scraggy"],
        "legendary": ["Cobalion", "Terrakion", "Keldeo", "Urshifu", "Zamazenta"]
    },
    "ice": {
        "common": ["Seel", "Snover", "Snorunt", "Spheal", "Vanillite"],
        "rare": ["Swinub", "Smoochum", "Sneasel", "Cubchoo", "Bergmite"],
        "legendary": ["Articuno", "Regice", "Kyurem", "Glastrier", "Calyrex"]
    }
}

# Market values by rarity
MARKET_VALUES = {
    "common": {"min": 5, "max": 50},
    "rare": {"min": 25, "max": 200},
    "legendary": {"min": 100, "max": 2000}
}

# Demo customer data
DEMO_CUSTOMERS = [
    {"name": "Ash Ketchum", "email": "ash@pokemon.com", "total_spent": 1250.99, "favorite_type": "electric", "join_date": "2024-01-15", "tier": "Elite"},
    {"name": "Misty Waterflower", "email": "misty@cerulean.gym", "total_spent": 890.50, "favorite_type": "water", "join_date": "2024-02-20", "tier": "Premium"},
    {"name": "Brock Harrison", "email": "brock@pewter.gym", "total_spent": 650.25, "favorite_type": "fighting", "join_date": "2024-03-10", "tier": "Standard"},
    {"name": "Gary Oak", "email": "gary@pallet.town", "total_spent": 2100.75, "favorite_type": "dragon", "join_date": "2023-12-01", "tier": "Elite"},
    {"name": "Dawn Berlitz", "email": "dawn@twinleaf.town", "total_spent": 750.00, "favorite_type": "fairy", "join_date": "2024-04-05", "tier": "Premium"},
    {"name": "Paul Shinji", "email": "paul@veilstone.city", "total_spent": 1500.99, "favorite_type": "dark", "join_date": "2024-01-30", "tier": "Elite"},
    {"name": "Serena Yvonne", "email": "serena@kalos.region", "total_spent": 950.25, "favorite_type": "psychic", "join_date": "2024-03-15", "tier": "Premium"},
    {"name": "Cynthia Shirona", "email": "cynthia@champion.league", "total_spent": 3500.00, "favorite_type": "dragon", "join_date": "2023-11-15", "tier": "VIP"}
]

# Contest data
ACTIVE_CONTESTS = [
    {
        "name": "Shiny Hunt Challenge",
        "description": "Find and showcase your rarest shiny Pokémon cards",
        "prize": "$500 Gift Card + Signed Charizard",
        "entries": 342,
        "end_date": "2025-06-15",
        "type": "showcase"
    },
    {
        "name": "Pack Break Prediction",
        "description": "Predict the next rare pull in our live stream",
        "prize": "Free Premium Membership",
        "entries": 156,
        "end_date": "2025-06-08",
        "type": "prediction"
    },
    {
        "name": "Collection Value Contest",
        "description": "Submit your collection for professional appraisal",
        "prize": "$1000 Cash Prize",
        "entries": 89,
        "end_date": "2025-06-20",
        "type": "appraisal"
    }
]

# Initialize session state
if 'customer_data' not in st.session_state:
    st.session_state.customer_data = DEMO_CUSTOMERS.copy()
if 'contest_entries' not in st.session_state:
    st.session_state.contest_entries = []
if 'sales_data' not in st.session_state:
    # Generate demo sales data
    sales_data = []
    for i in range(30):
        date = datetime.now() - timedelta(days=i)
        daily_sales = random.randint(500, 2500)
        sales_data.append({"date": date.strftime("%Y-%m-%d"), "sales": daily_sales})
    st.session_state.sales_data = sales_data

# Sidebar Navigation
st.sidebar.title("🎯 Poke Verse CRM")
st.sidebar.markdown("---")

page = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Dashboard", "🎮 Pokemon Explorer", "👥 Customer Management", "🏆 Contest Center", "📊 Analytics", "🔴 Live Whatnot", "⚙️ Settings"]
)

# Main content based on page selection
if page == "🏠 Dashboard":
    st.title("🏠 Poke Verse Ventures - Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", len(st.session_state.customer_data), "+12 this week")
    
    with col2:
        total_revenue = sum([customer["total_spent"] for customer in st.session_state.customer_data])
        st.metric("Total Revenue", f"${total_revenue:,.2f}", "+15.3%")
    
    with col3:
        active_contests = len(ACTIVE_CONTESTS)
        st.metric("Active Contests", active_contests, "+2 new")
    
    with col4:
        total_entries = sum([contest["entries"] for contest in ACTIVE_CONTESTS])
        st.metric("Contest Entries", total_entries, "+45 today")
    
    # Recent activity
    st.markdown("### 📈 Recent Activity")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔥 Hot Sales Today")
        st.success("🌟 Charizard Base Set - $1,200")
        st.info("⚡ Pikachu Promo - $350")
        st.warning("🌊 Blastoise 1st Edition - $850")
        
    with col2:
        st.markdown("#### 🎯 Contest Updates")
        for contest in ACTIVE_CONTESTS[:3]:
            st.write(f"🏆 **{contest['name']}** - {contest['entries']} entries")
    
    # Sales chart
    st.markdown("### 📊 Sales Trend (Last 30 Days)")
    df_sales = pd.DataFrame(st.session_state.sales_data)
    df_sales['date'] = pd.to_datetime(df_sales['date'])
    
    fig = px.line(df_sales, x='date', y='sales', title='Daily Sales Performance')
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")
    st.plotly_chart(fig, use_container_width=True)

elif page == "🎮 Pokemon Explorer":
    st.title("🎮 Pokémon Explorer & Investment Simulator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎒 Trainer Setup")
        username = st.text_input("Trainer Name", placeholder="Enter your name")
        poke_type = st.selectbox("Choose Pokémon Type", sorted(POKEMON_DATA.keys()))
        rarity = st.selectbox("Rarity Level", ["common", "rare", "legendary"])
        
        if st.button("🎲 Discover Pokémon", type="primary"):
            if username:
                chosen_pokemon = random.choice(POKEMON_DATA[poke_type][rarity])
                st.session_state.discovered_pokemon = chosen_pokemon
                st.session_state.pokemon_rarity = rarity
                st.session_state.pokemon_type = poke_type
    
    with col2:
        if 'discovered_pokemon' in st.session_state:
            pokemon = st.session_state.discovered_pokemon
            rarity = st.session_state.pokemon_rarity
            poke_type = st.session_state.pokemon_type
            
            st.markdown(f"### 🌟 You Discovered: **{pokemon}**")
            
            # Pokemon image (using placeholder URL structure)
            image_url = f"https://img.pokemondb.net/artwork/large/{pokemon.lower().replace(' ', '-')}.jpg"
            st.image(image_url, width=250)
            
            # Pokemon details
            st.info(f"**Type:** {poke_type.capitalize()} | **Rarity:** {rarity.capitalize()}")
            
            # Investment simulation
            st.markdown("#### 💰 Investment Simulator")
            min_val = MARKET_VALUES[rarity]["min"]
            max_val = MARKET_VALUES[rarity]["max"]
            
            if st.button("📈 Simulate Investment"):
                initial_cost = random.randint(min_val, max_val)
                months = random.randint(1, 24)
                growth_rate = random.uniform(0.8, 3.5) if rarity == "legendary" else random.uniform(0.9, 2.2)
                current_value = round(initial_cost * growth_rate, 2)
                profit = current_value - initial_cost
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Initial Cost", f"${initial_cost}")
                with col_b:
                    st.metric("Current Value", f"${current_value}")
                with col_c:
                    st.metric("Profit/Loss", f"${profit:+.2f}")
                
                if profit > 0:
                    st.success(f"🎉 Great investment! {pokemon} increased in value over {months} months!")
                    st.balloons()
                else:
                    st.warning(f"📉 Market downturn for {pokemon}. Hold for potential recovery!")

elif page == "👥 Customer Management":
    st.title("👥 Customer Management System")
    
    tab1, tab2, tab3 = st.tabs(["📋 Customer List", "➕ Add Customer", "🔍 Customer Analytics"])
    
    with tab1:
        st.markdown("### 📊 Customer Database")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            tier_filter = st.selectbox("Filter by Tier", ["All", "Standard", "Premium", "Elite", "VIP"])
        with col2:
            type_filter = st.selectbox("Filter by Favorite Type", ["All"] + sorted(POKEMON_DATA.keys()))
        with col3:
            min_spent = st.number_input("Minimum Spent ($)", min_value=0.0, value=0.0)
        
        # Filter customers
        filtered_customers = st.session_state.customer_data
        if tier_filter != "All":
            filtered_customers = [c for c in filtered_customers if c["tier"] == tier_filter]
        if type_filter != "All":
            filtered_customers = [c for c in filtered_customers if c["favorite_type"] == type_filter]
        filtered_customers = [c for c in filtered_customers if c["total_spent"] >= min_spent]
        
        # Display customers
        df_customers = pd.DataFrame(filtered_customers)
        st.dataframe(df_customers, use_container_width=True)
        
        st.write(f"Showing {len(filtered_customers)} of {len(st.session_state.customer_data)} customers")
    
    with tab2:
        st.markdown("### ➕ Add New Customer")
        
        with st.form("add_customer"):
            col1, col2 = st.columns(2)
            with col1:
                new_name = st.text_input("Customer Name")
                new_email = st.text_input("Email Address")
                new_spent = st.number_input("Total Spent ($)", min_value=0.0, value=0.0)
            with col2:
                new_type = st.selectbox("Favorite Pokémon Type", sorted(POKEMON_DATA.keys()))
                new_tier = st.selectbox("Customer Tier", ["Standard", "Premium", "Elite", "VIP"])
                new_date = st.date_input("Join Date", datetime.now())
            
            if st.form_submit_button("🎯 Add Customer", type="primary"):
                if new_name and new_email:
                    new_customer = {
                        "name": new_name,
                        "email": new_email,
                        "total_spent": new_spent,
                        "favorite_type": new_type,
                        "join_date": new_date.strftime("%Y-%m-%d"),
                        "tier": new_tier
                    }
                    st.session_state.customer_data.append(new_customer)
                    st.success(f"✅ Added {new_name} to customer database!")
                    st.balloons()
                else:
                    st.error("Please fill in name and email fields.")
    
    with tab3:
        st.markdown("### 📈 Customer Analytics")
        
        df_customers = pd.DataFrame(st.session_state.customer_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Tier distribution
            tier_counts = df_customers['tier'].value_counts()
            fig_tier = px.pie(values=tier_counts.values, names=tier_counts.index, 
                             title="Customer Distribution by Tier")
            st.plotly_chart(fig_tier, use_container_width=True)
        
        with col2:
            # Favorite type distribution
            type_counts = df_customers['favorite_type'].value_counts()
            fig_type = px.bar(x=type_counts.index, y=type_counts.values,
                             title="Popular Pokémon Types")
            st.plotly_chart(fig_type, use_container_width=True)
        
        # Spending analysis
        st.markdown("#### 💰 Customer Spending Analysis")
        fig_spending = px.histogram(df_customers, x='total_spent', nbins=10, 
                                   title="Customer Spending Distribution")
        st.plotly_chart(fig_spending, use_container_width=True)

elif page == "🏆 Contest Center":
    st.title("🏆 Contest Management Center")
    
    tab1, tab2, tab3 = st.tabs(["🎯 Active Contests", "📝 Contest Entries", "🎁 Create Contest"])
    
    with tab1:
        st.markdown("### 🔥 Active Contests")
        
        for i, contest in enumerate(ACTIVE_CONTESTS):
            with st.expander(f"🏆 {contest['name']} - {contest['entries']} entries"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Description:** {contest['description']}")
                    st.write(f"**Prize:** {contest['prize']}")
                    st.write(f"**Type:** {contest['type'].capitalize()}")
                    st.write(f"**Entries:** {contest['entries']}")
                
                with col2:
                    st.write(f"**Ends:** {contest['end_date']}")
                    days_left = (datetime.strptime(contest['end_date'], "%Y-%m-%d") - datetime.now()).days
                    if days_left > 0:
                        st.success(f"{days_left} days left")
                    else:
                        st.error("Contest ended")
                
                if st.button(f"View Entries for {contest['name']}", key=f"view_{i}"):
                    st.info("Entry management system would open here")
    
    with tab2:
        st.markdown("### 📋 Recent Contest Entries")
        
        # Mock entry data
        entry_data = [
            {"contest": "Shiny Hunt Challenge", "participant": "Ash Ketchum", "submission": "Shiny Charizard Card", "date": "2025-06-05"},
            {"contest": "Pack Break Prediction", "participant": "Misty Waterflower", "submission": "Predicted: Rare Gyarados", "date": "2025-06-04"},
            {"contest": "Collection Value Contest", "participant": "Gary Oak", "submission": "Complete Base Set", "date": "2025-06-03"},
        ]
        
        df_entries = pd.DataFrame(entry_data)
        st.dataframe(df_entries, use_container_width=True)
    
    with tab3:
        st.markdown("### 🎁 Create New Contest")
        
        with st.form("create_contest"):
            contest_name = st.text_input("Contest Name")
            contest_desc = st.text_area("Description")
            contest_prize = st.text_input("Prize Description")
            contest_type = st.selectbox("Contest Type", ["showcase", "prediction", "appraisal", "trivia"])
            contest_end = st.date_input("End Date")
            
            if st.form_submit_button("🚀 Launch Contest", type="primary"):
                if contest_name and contest_desc:
                    st.success(f"🎉 Contest '{contest_name}' created successfully!")
                    st.info("Contest would be added to active contests list")
                else:
                    st.error("Please fill in all required fields")

elif page == "📊 Analytics":
    st.title("📊 Business Analytics Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_customers = len(st.session_state.customer_data)
        st.metric("Total Customers", total_customers, "+8% this month")
    
    with col2:
        avg_spending = sum([c["total_spent"] for c in st.session_state.customer_data]) / len(st.session_state.customer_data)
        st.metric("Avg Customer Value", f"${avg_spending:.2f}", "+12.5%")
    
    with col3:
        total_entries = sum([contest["entries"] for contest in ACTIVE_CONTESTS])
        st.metric("Contest Engagement", total_entries, "+23%")
    
    # Revenue trends
    st.markdown("### 💰 Revenue Analysis")
    
    # Generate mock monthly data
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    revenue = [8500, 9200, 10100, 11500, 12800, 14200]
    
    fig_revenue = go.Figure()
    fig_revenue.add_trace(go.Scatter(x=months, y=revenue, mode='lines+markers', name='Revenue'))
    fig_revenue.update_layout(title="Monthly Revenue Trend", xaxis_title="Month", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_revenue, use_container_width=True)
    
    # Customer segmentation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Customer Segments")
        df_customers = pd.DataFrame(st.session_state.customer_data)
        tier_spending = df_customers.groupby('tier')['total_spent'].sum().reset_index()
        
        fig_segment = px.bar(tier_spending, x='tier', y='total_spent', 
                            title="Revenue by Customer Tier")
        st.plotly_chart(fig_segment, use_container_width=True)
    
    with col2:
        st.markdown("### 📈 Growth Metrics")
        st.success("🎯 Customer Retention: 94.2%")
        st.info("📦 Average Order Value: $127.50")
        st.warning("🔄 Repeat Purchase Rate: 78.3%")
        st.error("❌ Churn Rate: 5.8%")

elif page == "🔴 Live Whatnot":
    st.title("🔴 Live Whatnot Integration")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📺 Live Stream Dashboard")
        st.info("🔴 **LIVE NOW:** Friday Night Pokemon Pack Breaks!")
        
        # Mock live stats
        st.markdown("#### 📊 Live Stats")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Viewers", "1,247", "+156")
        with col_b:
            st.metric("Bids Placed", "89", "+12")
        with col_c:
            st.metric("Revenue", "$2,340", "+$450")
        
        # Recent sales
        st.markdown("#### 🎯 Recent Sales")
        live_sales = [
            {"item": "Charizard Base Set Holo", "price": "$850", "buyer": "Trainer_Mike"},
            {"item": "Pikachu Promo Card", "price": "$320", "buyer": "PokeFan_Sarah"},
            {"item": "Blastoise 1st Edition", "price": "$650", "buyer": "CollectorGary"},
        ]
        
        for sale in live_sales:
            st.success(f"💰 **{sale['item']}** sold for **{sale['price']}** to {sale['buyer']}")
    
    with col2:
        st.markdown("### 🎁 Live Features")
        
        st.markdown("#### 🎰 Giveaway Wheel")
        if st.button("🎲 Spin for Prize"):
            prizes = ["$50 Gift Card", "Free Pack", "Rare Sticker", "Entry Ticket", "Better luck next time!"]
            prize = random.choice(prizes)
            st.success(f"🎉 You won: {prize}")
        
        st.markdown("#### 📢 Announcements")
        st.info("🎯 Next giveaway in 8 minutes!")
        st.warning("⏰ Rare card auction starting soon")
        st.success("🔥 Chat milestone reached!")
        
        st.markdown("#### 📈 Upcoming Shows")
        st.write("📅 **Saturday 2PM:** Vintage Pack Opening")
        st.write("📅 **Sunday 6PM:** Graded Card Auction")
        st.write("📅 **Monday 8PM:** Modern Set Reviews")

elif page == "⚙️ Settings":
    st.title("⚙️ System Settings")
    
    tab1, tab2, tab3 = st.tabs(["🎨 Appearance", "🔔 Notifications", "💾 Data Management"])
    
    with tab1:
        st.markdown("### 🎨 Appearance Settings")
        theme = st.selectbox("Choose Theme", ["Light", "Dark", "Auto"])
        show_animations = st.checkbox("Enable Animations", value=True)
        compact_mode = st.checkbox("Compact Mode", value=False)
        
        if st.button("💾 Save Appearance"):
            st.success("Appearance settings saved!")
    
    with tab2:
        st.markdown("### 🔔 Notification Settings")
        email_notifications = st.checkbox("Email Notifications", value=True)
        contest_alerts = st.checkbox("Contest Entry Alerts", value=True)
        sales_notifications = st.checkbox("Sales Notifications", value=True)
        whatnot_alerts = st.checkbox("Whatnot Live Alerts", value=True)
        
        if st.button("🔔 Save Notifications"):
            st.success("Notification settings saved!")
    
    with tab3:
        st.markdown("### 💾 Data Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📤 Export Data")
            if st.button("📊 Export Customer Data"):
                st.info("Customer data would be exported as CSV")
            if st.button("📈 Export Analytics"):
                st.info("Analytics data would be exported")
        
        with col2:
            st.markdown("#### 🔄 Reset Options")
            if st.button("🗑️ Clear Demo Data", type="secondary"):
                st.session_state.customer_data = []
                st.success("Demo data cleared!")
            if st.button("🔄 Reset All Settings", type="secondary"):
                st.warning("All settings would be reset to defaults")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎯 <strong>Poke Verse Ventures CRM</strong> | Powered by Streamlit</p>
    <p>📧 Contact: admin@pokeverseventures.com | 🌐 <a href="https://www.whatnot.com/">Visit us on Whatnot</a></p>
    <p>© 2025 Poke Verse Ventures. Gotta manage 'em all! 🎮</p>
</div>
""", unsafe_allow_html=True)

