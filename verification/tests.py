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
            "input": (0, '478103487120470129'),
            "answer": True,
            "explanation": [
                "                 0",
                "000000000000000000",
                "478103487120470129",
                "DDDDDDDDDDDDDDDDDD",
                "VVVVVVVVVVVVVVVVVV"]},
        {
            "input": (127, 'Checkio'),
            "answer": True,
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
            "input": (0, '0'),
            "answer": True,
            "explanation": [
                "0",
                "0",
                "0",
                "D",
                "V"]},

        {
            "input": (0, '012345678901234567890'),
            "answer": True,
            "explanation": [
                "                    0",
                "000000000000000000000",
                "012345678901234567890",
                "DDDDDDDDDDDDDDDDDDDDD",
                "VVVVVVVVVVVVVVVVVVVVV"]},

        {
            "input": (1, 'A'),
            "answer": True,
            "explanation": [
                "1",
                "1",
                "A",
                "L",
                "V"]},

        {
            "input": (1, '1'),
            "answer": False,
            "explanation": [
                "1",
                "1",
                "1",
                "D",
                "X"]},

        {
            "input": (1, 'z'),
            "answer": True,
            "explanation": [
                "1",
                "1",
                "z",
                "L",
                "V"]},

        {
            "input": (4294967295, 'LoremIpsumDoLorsiTametConsectet'),
            "answer": False,
            "explanation": [
                "                     4294967295",
                "11111111111111111111111111111111",
                "LoremIpsumDoLorsiTametConsectet",
                "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
                "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"]},

        {
            "input": (1, 'LoremIpsumDoLorsiTametConsectet'),
            "answer": False,
            "explanation": [
                "                              1",
                "0000000000000000000000000000001",
                "LoremIpsumDoLorsiTametConsectet",
                "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXV"]},

        {
            "input": (4294967295, 'Loremipsumdolorsitametconsecte9'),
            "answer": False,
            "explanation": [
                "                     4294967295",
                "11111111111111111111111111111111",
                "Loremipsumdolorsitametconsecte9",
                "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLD",
                "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX"]},


    ]
}
