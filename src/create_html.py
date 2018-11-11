import webbrowser

# 更新建议 使用模板引擎，将HTML和python代码分开

HTML = "demo_1.html"  # 命名生成的html

f = open(HTML, 'w')
message = """
<html>
<head>
<script
 type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
 </script>
</head>
<body>
<script type="text/javascript">
    MathJax.Hub.Config({
        extensions: ["tex2jax.js"],
        jax: ["input/TeX", "output/HTML-CSS"],
        tex2jax: {
            inlineMath: [["\\(", "\\)"]],
            displayMath: [["$$", "$$"],["\\[", "\\]"]],
            processEscapes: true
        },
        "HTML-CSS": { availableFonts: ["TeX"] }
    });
</script>
<p>
$$\\begin{cases}
a_1x+b_1y+c_1z=d_1 \\\ 
a_2x+b_2y+c_2z=d_2 \\\ 
a_3x+b_3y+c_3z=d_3 
\end{cases}
$$
</p>
</body>
</html>"""

f.write(message)
f.close()

webbrowser.open(HTML, new=1)
