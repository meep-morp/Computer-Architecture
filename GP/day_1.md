<style>
@import url('https://fonts.googleapis.com/css2?family=Kufam&display=swap');

* {
    font-family: 'Kufam', cursive;
    text-align: center;
}

ul, li {
    text-align: left;
}

h2, h3 {
    text-decoration: underline;
}

li em {
    margin-right: 7px;
}

.chart li {
    margin-bottom: 8px;
}
</style>

<h1>Number Bases</h1>

---

<em>It's the 'language' that a number is written down in.</em>

<img src="./binary_to_Decimal.png">

<h3>Types</h3>

<ul>
<li>Base 2: Binary</li>
<li>Base 8: Octal</li>
<li>Base 10: decimal</li>
<li>Base 16: hexadecimal</li>
<li>Base 64: Base 64</li>
</ul>

<h2>Binary</h2>

<em>Binary digit == "bit"</em>

<p>Computers think in 0s and 1s.</p>
<p>The 0 and 1 represents whether or not a certain circuit has electricity present. This can be interpreted as a number. These numbers are then transported to a 'logic gate' The logic gate then performs arithmetic on the number.</p>

<a href="https://circuitverse.org/">Circuit Simulator</a>

<h3>Prefix in Code</h3>

<ul>
<li>0b: Binary</li>
<li>0x: hexadecimal</li>
<li>0o: Octal</li>
</ul>

```

print(0b11000 == 0x18)
True

```

<h2>Conversions</h2>

<a href="https://cheatography.com/deleted-56036/cheat-sheets/data-representation-aqa-computer-science/">Useful
chart for conversions</a>

<ul class="chart">
<li><em>Denary to Binary:</em> Divide by 2, then read the remainders backwards.</li>
<li><em>Binary to Denary:</em> Multiply the binary numbers (i.e. every single digit) by the relevant place value, then add all of these together.</li>
<li><em>Denary to Hexadecimal:</em>Divide by 16, then read the divisors and remainder backwards. Then convert digits to hex digits.</li>
<li><em>Hexa­dec­imal to Denary:</em>Separate the hex digits, convert each digit to binary, concat­enate, then convert to denary</li>
<li><em>Binary to Hexa­dec­imal:</em>Convert to denary, then hex.</li>
<li><em>Hexa­dec­imal to Binary:</em>Convert to denary, then binary.</li>
</ul>

<h2>Hexadecimal</h2>

```

#ff12d9

```

<p>Colors are a popular form of Hexadecimal</p>
<p>255 is the largest number that can be stored in a single byte</p>

<hr>

<h1>Computing</h1>
<a href="https://en.wikipedia.org/wiki/Turing_completeness">Turing Completeness</a>
<p>
<iframe width="420" height="315" src="https://www.youtube.com/watch?v=RPQD7-AOjMI"></iframe>
</p>
<p>ComputerPhile -- Turing Completeness</p>

<ul>
<li>Operand -- Arguments</li>
</ul>
