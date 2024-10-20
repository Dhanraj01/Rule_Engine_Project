
const createRule = async () => {
    const rule = document.getElementById('rule-input').value;  
    console.log(rule)
    try {
        const response = await axios.post('http://127.0.0.1:3000/create_rule', {
            rule_string: rule
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.status === 201) {
            alert('Rule created successfully!');
        }
    } catch (error) {
        console.error('Error creating rule:', error);
        alert('Failed to create rule');
    }
};


document.getElementById('create-rule-btn').addEventListener('click', createRule);
