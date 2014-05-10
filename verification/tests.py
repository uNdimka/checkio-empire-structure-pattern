"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": (42, '12a0b3e4'),
            "answer": True,
            "explanation": [
                "      42",
                "00101010",
                "12a0b3e4",
                "DDLDLDLD",
                "VVVVVVVV"]
        },

        {
            "input": (101, 'ab23b4zz'),
            "answer": False,
            "explanation": [
                "     101",
                "01100101",
                "ab23b4zz",
                "LLDDLDLL",
                "XVXVXXXV"]
        },

        {
            "input": (127, 'Сheckio'),
            "answer": False,
            "explanation": [
                "    127",
                "1111111",
                "Сheckio",
                "LLLLLLL",
                "VVVVVVV"]},

        {
            "input": (7, 'Hello'),
            "answer": False,
            "explanation": [
                "    7",
                "00111",
                "Hello",
                "LLLLL",
                "XXVVV"]},

    ],
    "Edge": [
        {
            "input": (0, "0"),
            "answer": True,
            "explanation": ""
        },
        {
            "input": (0, "012345678901234567890"),
            "answer": True,
            "explanation": ""
        },
        {
            "input": (1, "A"),
            "answer": True,
            "explanation": ""
        },
        {
            "input": (1, "1"),
            "answer": False,
            "explanation": ""
        },
        {
            "input": (1, "z"),
            "answer": True,
            "explanation": ""
        },
        {
            "input": (2 ** 32 - 1, "LoremIpsumDoLorsiTametConsectet"),
            "answer": True,
            "explanation": ""
        },
        {
            "input": (2 ** 32 - 1, "Loremipsumdolorsitametconsecte9"),
            "answer": False,
            "explanation": ""
        },


    ]
}
