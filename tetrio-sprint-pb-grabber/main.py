# API Call for the TETR.IO Sprint Leaderboard
import requests
session_id = "sprintpb-grabber"

headers = {
    "X-Session-ID": session_id,
    "User-Agent": "Mozilla/5.0"
}

tetra_channel_url = "https://ch.tetr.io/api/"

def get_tetrio_sprint_pb(name):
    url = f"{tetra_channel_url}users/{name}/summaries/40l"

    response = requests.get(url, headers=headers)
    return response.json()

# Main
player_info = ["", 0, "?", "", "", "", "", 0, 0]


fileList = "input.txt"
count = 0

with open (fileList, "r") as usernameInput:

    # counts the amount of lines in the input.txt file with the iterable parameter
    line_count = sum(1 for line in usernameInput)

    # creates an array with the length as the line amount
    players_ouput = [""] * line_count

    # resets the pointer when reading the file
    usernameInput.seek(0)
    
    for username in usernameInput:
        name = username.strip()
        


# ask for their username
#name = input("Enter a username: ")
        name = name.lower()
        raw_info = get_tetrio_sprint_pb(name)

        # username
        player_info[0] = raw_info["data"]["record"]["user"]["username"]
        # sprint time
        player_info[1] = round((raw_info["data"]["record"]["results"]["stats"]["finaltime"] / 1000), 3)
        # country (code)
        countryCode = raw_info["data"]["record"]["user"]["country"]


        # list of every country with their respective continents in a hashmap
        Africa = {"DZ": "Algeria", "AO": "Angola", "BJ": "Benin", "BW": "Botswana", "BF": "Burkina Faso", "BI": "Burundi", "CV": "Cape Verde", "CM": "Cameroon", "CF": "Central African Republic", "TD": "Chad", "KM": "Comoros", "CG": "Congo", "CD": "Democratic Republic of the Congo", "DJ": "Djibouti", "EG": "Egypt", "GQ": "Equatorial Guinea", "ER": "Eritrea", "SZ": "Eswatini", "ET": "Ethiopia", "GA": "Gabon", "GM": "Gambia", "GH": "Ghana", "GN": "Guinea", "GW": "Guinea-Bissau", "CI": "Ivory Coast", "KE": "Kenya", "LS": "Lesotho", "LR": "Liberia", "LY": "Libya", "MG": "Madagascar", "MW": "Malawi", "ML": "Mali", "MR": "Mauritania", "MU": "Mauritius", "YT": "Mayotte", "MA": "Morocco", "MZ": "Mozambique", "NA": "Namibia", "NE": "Niger", "NG": "Nigeria", "RE": "Réunion", "RW": "Rwanda", "SH": "Saint Helena", "ST": "Sao Tome and Principe", "SN": "Senegal", "SC": "Seychelles", "SL": "Sierra Leone", "SO": "Somalia", "ZA": "South Africa", "SS": "South Sudan", "SD": "Sudan", "TZ": "Tanzania", "TG": "Togo", "TN": "Tunisia", "UG": "Uganda", "EH": "Western Sahara", "ZM": "Zambia", "ZW": "Zimbabwe"}
        Asia = {"AF": "Afghanistan", "AM": "Armenia", "AZ": "Azerbaijan", "BH": "Bahrain", "BD": "Bangladesh", "BT": "Bhutan", "BN": "Brunei", "KH": "Cambodia", "CN": "China", "CY": "Cyprus", "GE": "Georgia", "IN": "India", "ID": "Indonesia", "IR": "Iran", "IQ": "Iraq", "IL": "Israel", "JP": "Japan", "JO": "Jordan", "KZ": "Kazakhstan", "KW": "Kuwait", "KG": "Kyrgyzstan", "LA": "Laos", "LB": "Lebanon", "MY": "Malaysia", "MV": "Maldives", "MN": "Mongolia", "MM": "Myanmar", "NP": "Nepal", "KP": "North Korea", "OM": "Oman", "PK": "Pakistan", "PS": "Palestine", "PH": "Philippines", "QA": "Qatar", "SA": "Saudi Arabia", "SG": "Singapore", "KR": "South Korea", "LK": "Sri Lanka", "SY": "Syria", "TW": "Taiwan", "TJ": "Tajikistan", "TH": "Thailand", "TL": "Timor-Leste", "TR": "Turkey", "TM": "Turkmenistan", "AE": "United Arab Emirates", "UZ": "Uzbekistan", "VN": "Vietnam", "YE": "Yemen"}
        Europe = {"AL": "Albania", "AD": "Andorra", "AT": "Austria", "BY": "Belarus", "BE": "Belgium", "BA": "Bosnia and Herzegovina", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus", "CZ": "Czechia", "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France", "DE": "Germany", "GR": "Greece", "HU": "Hungary", "IS": "Iceland", "IE": "Ireland", "IT": "Italy", "XK": "Kosovo", "LV": "Latvia", "LI": "Liechtenstein", "LT": "Lithuania", "LU": "Luxembourg", "MT": "Malta", "MD": "Moldova", "MC": "Monaco", "ME": "Montenegro", "NL": "Netherlands", "MK": "North Macedonia", "NO": "Norway", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "RU": "Russia", "SM": "San Marino", "RS": "Serbia", "SK": "Slovakia", "SI": "Slovenia", "ES": "Spain", "SE": "Sweden", "CH": "Switzerland", "UA": "Ukraine", "GB": "United Kingdom", "VA": "Vatican City"}
        North_America = {"AG": "Antigua and Barbuda", "BS": "Bahamas", "BB": "Barbados", "BZ": "Belize", "CA": "Canada", "CR": "Costa Rica", "CU": "Cuba", "DM": "Dominica", "DO": "Dominican Republic", "SV": "El Salvador", "GD": "Grenada", "GT": "Guatemala", "HT": "Haiti", "HN": "Honduras", "JM": "Jamaica", "MX": "Mexico", "NI": "Nicaragua", "PA": "Panama", "KN": "Saint Kitts and Nevis", "LC": "Saint Lucia", "VC": "Saint Vincent and the Grenadines", "TT": "Trinidad and Tobago", "US": "United States"}
        South_America = {"AR": "Argentina", "BO": "Bolivia", "BR": "Brazil", "CL": "Chile", "CO": "Colombia", "EC": "Ecuador", "GY": "Guyana", "PY": "Paraguay", "PE": "Peru", "SR": "Suriname", "UY": "Uruguay", "VE": "Venezuela"}
        Oceania = {"AU": "Australia", "FJ": "Fiji", "KI": "Kiribati", "MH": "Marshall Islands", "FM": "Micronesia", "NR": "Nauru", "NZ": "New Zealand", "PW": "Palau", "PG": "Papua New Guinea", "WS": "Samoa", "SB": "Solomon Islands", "TO": "Tonga", "TV": "Tuvalu", "VU": "Vanuatu"}


        # finds the correct continent and translate to the full country name
        if countryCode in Africa:
            player_info[2] = Africa[countryCode]
            player_info[3] = "Africa"
            
        elif countryCode in Asia:
            player_info[2] = Asia[countryCode]
            player_info[3] = "Asia"
            
        elif countryCode in Europe:
            player_info[2] = Europe[countryCode]
            player_info[3] = "Europe"
            
        elif countryCode in North_America:
            player_info[2] = North_America[countryCode]
            player_info[3] = "North America"
            
        elif countryCode in South_America:
            player_info[2] = South_America[countryCode]
            player_info[3] = "South America"
            
        elif countryCode in Oceania:
            player_info[2] = Oceania[countryCode]
            player_info[3] = "Oceania"
        else:
            player_info[2] = "?"
            player_info[3] = "?"

        # date submitted (in UTC)
        raw_time = raw_info["data"]["record"]["ts"]
        raw_time = raw_time[0:10]
        player_info[4] = f"{raw_time[6:7]}/{raw_time[9:10]}/{raw_time[0:4]}"

        # replay link (TETR.IO)
        player_info[5] = f"https://tetr.io/#R:{raw_info["data"]["record"]["replayid"]}"

        # client (TETR.IO)
        player_info[6] = "TETR.IO"

        # blocks
        player_info[7] = raw_info["data"]["record"]["results"]["stats"]["piecesplaced"]

        # pps
        player_info[8] = round((raw_info["data"]["record"]["results"]["aggregatestats"]["pps"]), 2)

    

        # Output
        players_ouput[count] = player_info
        count = count + 1

        
        for result in player_info:
            print(str(result)) # prevents a newline

        print()
        print()
        
