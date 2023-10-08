async function getPublicKey() {
  const response = await fetch('/generate_key/', {
    method: 'POST'
  });
  const data = await response.json();
  return data.key;
}

async function encryptData(data) {
  const response = await fetch('/encrypt_data/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ data: data })
  });
  const encryptedData = await response.json();
  return encryptedData.encrypted_data;
}

async function decryptData(encryptedData) {
  const response = await fetch('/decrypt_data/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ data: encryptedData })
  });
  const decryptedData = await response.json();
  return decryptedData.decrypted_data;
}

function checkResponse(response) {
  if (response.status === 400) {
    alert('Cross-origin request detected!');
  }
}

