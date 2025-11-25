
<h1>🎰 Anime Character Spinner</h1>

<p>
This project is a Gacha-style anime character spinner made with Python and Tkinter. 
The user can spin up to <b>20 times</b>, and each spin selects a random character based on predefined rarity chances.
</p>

<hr>

<h2>📌 How the Program Works</h2>

<h3>1️⃣ Character Selection System</h3>
<p>
The program uses a class named <code>Characters</code>, which includes six functions:
</p>

<ul>
    <li>common()</li>
    <li>uncommon()</li>
    <li>rare()</li>
    <li>epic()</li>
    <li>legendry()</li>
    <li>mythic()</li>
</ul>

<p>
Each function:
</p>

<ul>
    <li>Contains a list of anime characters</li>
    <li>Defines probability weights for selection</li>
    <li>Uses <code>random.choices()</code> to pick one character</li>
</ul>

<hr>

<h3>2️⃣ Rarity Chances</h3>

<p>
When the user clicks the <b>Spin</b> button, the program selects a rarity based on the following chances:
</p>

<table border="1" cellpadding="6" cellspacing="0">
    <tr>
        <th>Rarity</th>
        <th>Chance (%)</th>
    </tr>
    <tr><td>Common</td><td>62%</td></tr>
    <tr><td>Uncommon</td><td>20%</td></tr>
    <tr><td>Rare</td><td>10%</td></tr>
    <tr><td>Epic</td><td>5%</td></tr>
    <tr><td>Legendary</td><td>2.5%</td></tr>
    <tr><td>Mythic</td><td>0.5%</td></tr>
</table>

<p>
After selecting a rarity group, one character from that category is randomly chosen.
</p>

<hr>

<h3>3️⃣ Visual Spin Animation</h3>

<p>
Before showing the final character, the program displays a short animation that cycles through fake character names and colors, giving the feeling of a real spinner wheel. After the animation finishes, the real selected character appears.
</p>

<hr>

<h3>4️⃣ Rarity Colors</h3>

<p>
Each rarity result is displayed in a specific color:
</p>

<table border="1" cellpadding="6" cellspacing="0">
    <tr>
        <th>Rarity</th>
        <th>Display Color</th>
    </tr>
    <tr><td>Common</td><td>Gray</td></tr>
    <tr><td>Uncommon</td><td>Green</td></tr>
    <tr><td>Rare</td><td>Blue</td></tr>
    <tr><td>Epic</td><td>Purple</td></tr>
    <tr><td>Legendary</td><td>Orange</td></tr>
    <tr><td>Mythic</td><td>Red</td></tr>
</table>

<hr>

<h3>5️⃣ User Interface (GUI)</h3>

<p>
The program uses Tkinter and includes:
</p>

<ul>
    <li>A <b>Spin</b> button</li>
    <li>An <b>Exit</b> button</li>
    <li>A label showing the result</li>
    <li>A counter showing how many spins are left</li>
</ul>

<p>
The user starts with <b>20 spins</b>. When the counter reaches zero, spinning stops.
</p>

<hr>

<h2>📁 Requirements</h2>

<p>
No external libraries are needed. It uses:
</p>

<ul>
    <li><code>tkinter</code></li>
    <li><code>random</code></li>
</ul>

<p>
Both are included with standard Python installations. The program works on Python <b>3.7+</b>.
</p>

<hr>

<h2>▶ Running the Program</h2>

<pre>
python main.py
</pre>

<hr>

<h2>✔ Project Structure</h2>

<pre>
Anime-Character-Spinner/
│
├── main.py
└── README.md
</pre>

<hr>

</body>
</html>
