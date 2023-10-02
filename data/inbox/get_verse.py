from flask import Flask, request, jsonify

app = Flask(__name__)

gita_data = [
    {
        "VerseID": "1.1",
        "Functionality": "Query",
        "RelatedFunctions": ["DecisionMaking", "ConflictResolution"]
    },
    {
        "VerseID": "2.47",
        "Functionality": "Execution",
        "RelatedFunctions": ["GoalSetting", "Detachment"]
    }
]

@app.route('/getVerseFunction', methods=['GET'])
def get_verse_function():
    verse_id = request.args.get('verseID')
    verse_data = next((item for item in gita_data if item["VerseID"] == verse_id), None)
    if verse_data:
        return jsonify(verse_data)
    else:
        return jsonify({"error": "Verse not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
