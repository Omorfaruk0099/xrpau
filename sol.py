# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCByYW5kb20KaW1wb3J0IHRpbWUKaW1wb3J0IGJzNAppbXBvcnQgc3lzCmltcG9ydCBvcwoKcyA9IHJlcXVlc3RzLlNlc3Npb24oKQoKYmFubmVyID0gIiIiXDAzM1swOzBtCistLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rCisgICAgICAgXDAzM1swMTszMm1DWVJBWCBQWVRIT04gU0NSSVBUXDAzM1swOzBtICAgICAgICsKKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSsKKyAgICAgICAgIFwwMzNbMDE7MzRtU09MIEFVVE8gRkFVQ0VUXDAzM1swOzBtICAgICAgICAgKworKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKworKioqKioqKioqKioqXDAzM1swMTszMW1ZT1VUVUJFXDAzM1swOzBtKioqKioqKioqKioqKiorCisgIGh0dHBzOi8veW91dHViZS5jb20vQGN5cmF4dHYyMSArCistLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rCisqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiorIiIiCgpkZWYgY291bnRkb3duKHQpOgoJd2hpbGUgdDoKCQltaW5zLCBzZWNzID0gZGl2bW9kKHQsIDYwKQoJCXRpbWVyID0gJ3s6MDJkfTp7OjAyZH0nLmZvcm1hdChtaW5zLCBzZWNzKQoJCXByaW50ICgiXDAzM1swMTszMm1bKl0gcGxlYXNlIHdhaXQ6XDAzM1swOzBtIiwgdGltZXIsIGVuZD0iXHIiKQoJCXRpbWUuc2xlZXAoMSkKCQl0IC09IDEKCmRlZiBib3QoKToKCXRyeToKCQloZWFkZXJzID0gewoJCQkidXNlci1hZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTE0LjAuMC4wIFNhZmFyaS81MzcuMzYiCgkJCX0KCQkKCQliID0gcy'
love = '5aMKDbVzu0qUOmBv8ioUEwn2yhMl50o3NiMzS1L2I0Y2A1paWyozA5Y3AioPVfVTuyLJEypaZ9nTIuMTIlplxXPDymo3IjVQ0tLaZ0YxWyLKI0nJM1oSAiqKNbLv50MKu0YPNvnUEgoP5jLKWmMKVvXDbWPJyzVUAiqKNhMzyhMPtvMTy2VvjtrlWwoTSmplV6VPWuoTIlqPOuoTIlqP1xLJ5aMKVtqTI4qP1wMJ50MKVvsFx6PtxWPKOlnJ50VPtvKQNmZ1fjZGfmZJ1osy0tMTScoUxtL2kunJ0toTygnKDtMz9lVUEbnKZtL29covOlMJSwnTIxYPOjoTIup2HtL29gMJWuL2ftLJqunJ4tqT9go3Wlo3phKT5pZQZmJmN7ZT0vXDbWPDymrKZhMKucqPtcPtxWMJkmMGbXPDxWnJLtp291pP5znJ5xXPWmpTShVvjtrlWwoTSmplV6VPWvLJEaMFOvLJEaMF1xLJ5aMKVvsFx6PtxWPDyjpzyhqPNbVyjjZmAoZQR7ZmSgJ35qVTS1qT8tMzS1L2I0VTWuoTShL2HtMJ1jqUypoyjjZmAoZQfjoFVcPtxWPDymrKZhMKucqPtcPtxWPJIfp2H6PtxWPDywoTScoFN9VUAiqKNhMzyhMPtvMTy2VvjtrlWwoTSmplV6VPW0MKu0YKqupz5cozptL29fVa0cPtxWPDywoTScoKAsoTIzqPN9VPtvVPVhnz9covuwoTScoF50MKu0YaAjoTy0XPxcXDbWPDxWp2IwVQ0tp291pP5znJ5xXPWvVvjtrlWcMPV6VPWmMJAiozDvsFxXPDxWPJMuqJAyqS90o2gyovN9VUAiqKNhMzyhMPtvnJ5jqKDvYPO7Vz5uoJHvBvNvLKI0o19zLKIwMKEsqT9eMJ4vsFyoVaMuoUIyVy0XPDxWPJAmpzMsqT9eMJ4tCFOmo3IjYzMcozDbVzyhpUI0VvjtrlWcMPV6VPW0o2gyovW9XIfvqzSfqJHvKDbWPDxWqT9eMJ4tCFOmo3IjYzMcozDbVzyhpUI0VvjtrlWhLJ1yVwbtVaEin2IhVa0cJlW2LJk1MFWqPtxWPDxXPDxWPJAiqJ50MT93ovucoaDbp2IwYaEyrUDcXDbWPDxWPtxWPDyxLKEuVQ0trjbWPDxWPFWuqKEiK2Mu'
god = 'dWNldF90b2tlbiI6IGZhdWNldF90b2tlbiwKCQkJCQkiY3NyZl90b2tlbl9uYW1lIjogY3NyZl90b2tlbiwKCQkJCQkidG9rZW4iOiB0b2tlbgoJCQkJCX0KCQkJCWwgPSBzLnBvc3QoImh0dHBzOi8vbHRja2luZy50b3AvZmF1Y2V0L3ZlcmlmeS9zb2wiLCBoZWFkZXJzPWhlYWRlcnMsIGRhdGE9ZGF0YSkKCQkJCQoJCQkJY2wgPSAoY2xhaW1zX2xlZnQucmVwbGFjZSgiY2xhaW1zIGxlZnQiLCAiIikpCgkJCQlwcmludCAoIlwwMzNbMDE7MzJtWypdIDAuMDAwMDAxNDkgU09MIHNlbnQgdG8geW91ciBmYXVjZXRwYXkgYWNjb3VudFwwMzNbMDswbSBbJXMgY2xhaW1zIGxlZnRdIiAlIChjbCkpCgkJCQlib3QoKQoJCQoJZXhjZXB0IFR5cGVFcnJvcjoKCQlib3QoKQoJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOgoJCXByaW50ICgiXDAzM1swMTszMW1bfl0gY29ubmVjdGlvbiBlcnJvci4gLiAucmV0cnlpbmdcMDMzWzA7MG0iKQoJCWJvdCgpCglleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CgkJcHJpbnQgKCJbKl1cMDMzWzAxOzMxbVt+XSB1c2VyIHNodXRkb3duLi4uXG5cMDMzWzA7MG0iKQoJCXN5cy5leGl0KCkKCmRlZiBsb2dpbigpOgoJdHJ5OgoJCWhlYWRlcnMgPSB7CgkJCSJ1c2VyLWFnZW50IjogIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIKCQkJfQoJCQoJCXIgPSBzLmdldCgiaHR0cHM6Ly9sdGNraW5nLnRvcC8/cj00NzUiLCBoZWFkZXJzPWhlYWRlcnMpCgkJc291cCA9IGJzNC5CZWF1dGlmdWxTb3VwKHIudGV4dCwgImh0bWwucGFyc2VyIikKCQl0b2'
destiny = 'gyovN9VUAiqKNhMzyhMPtvnJ5jqKDvYPO7VzyxVwbtVaEin2IhVa0cJlW2LJk1MFWqPtxWPtxWpTS5oT9uMUZtCFO7PtxWPFW3LJkfMKDvBvOyoJScoPjXPDxWVzAmpzMsqT9eMJ5sozSgMFV6VUEin2IhPtxWPK0XPDxXPDy0nJ1yYaAfMJIjXQRcPtxWPtxWoT9anJ4tCFOmYaOip3DbVzu0qUOmBv8ioUEwn2yhMl50o3NiLKI0nP9fo2qcovVfVTuyLJEypaZ9nTIuMTIlpljtMTS0LG1jLKyfo2SxplxXPDy0nJ1yYaAfMJIjXQRcPtxWnJLtoT9anJ4hp3EuqUImK2AiMTHtCG0tZwNjBtbWPDywo3IhqTEiq24bnJ50XQZcXDbWPDyjpzyhqPNbVyjjZmAoZQR7ZmWgJlcqJ0EiozIqJ2kiM2yhVUA1L2Ayp3AzqJkfrI0vXDbWPDyvo3DbXDbWPJIfp2H6PtxWPKOlnJ50VPtvKQNmZ1fjZGfmZJ1oMKWlo3WqJ2kiM2yhVTMunJkyMS0vXDbWPDyjpzyhqPNbVyg+KFOwnTIwnlO5o3IlVTyhpUI0VTIgLJyfVTShMPOcoaEypz5yqPOwo25hMJA0nJ9hKQNmZ1fjBmOgKT4vXDbWPDymrKZhMKucqPtcPtyyrTAypUDtIUyjMHIlpz9lBtbWPJkiM2yhXPxXPJI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPDyjpzyhqPNbVyjjZmAoZQR7ZmSgJ35qVTAioz5yL3Eco24tMKWlo3VhVP4tYaWyqUW5nJ5aKQNmZ1fjBmOgVvxXPDyfo2qcovtcPtyyrTAypUDtF2I5Lz9upzEWoaEypaW1pUD6PtxWpUWcoaDtXPWoXy1pZQZmJmNkBmZkoIg+KFO1p2IlVUAbqKExo3qhYv4hKT5pZQZmJmN7ZT0vXDbWPKA5pl5yrTy0XPxXPzyzVS9sozSgMI9sVQ09VPWsK21unJ5sKlV6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKOlnJ50VPuvLJ5hMKVcPtyyoJScoPN9VTyhpUI0XPWpZQZmJmNkBmZloIfdKFOzLKIwMKEjLKxtMJ1unJj6KQNmZ1fjBmOgVPVcPtyfo2qcovtc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))