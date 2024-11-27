// Ensure document has fully loaded before executing functions
window.onload = function() {
  // Display the dashboard and load past records
  showDashboard();
};

// Define `openContractModal` to handle "View Contracts" button click
function openContractModal() {
  // Check if element exists and display a modal or list of contracts
  const contractList = document.getElementById('contract-list');
  if (contractList) {
    contractList.innerHTML = "<p>No new contracts available at this moment.</p>";
  } else {
    console.error("Element with id 'contract-list' not found.");
  }
}

// Check if `getStorageInfo` is linked properly to storage output element
function getStorageInfo() {
  const storageOutput = document.getElementById('storage-output');
  if (storageOutput) {
    storageOutput.innerHTML = `
      <p><strong>Nearby Storage Units:</strong> 5</p>
      <p><strong>Available Capacity:</strong> 20,000 tons</p>
      <p><strong>Distance:</strong> 15 km</p>
    `;
  } else {
    console.error("Element with id 'storage-output' not found.");
  }
}

// Define `loadPastRecords` only if records-list element exists
function loadPastRecords() {
  const recordsList = document.getElementById('records-list');
  if (recordsList) {
    const records = [
      { buyer: 'Retailer ABC', price: '₹15/kg', status: 'Completed' },
      { buyer: 'Supermarket XYZ', price: '₹17/kg', status: 'Ongoing' },
      { buyer: 'Local Farmers Co-op', price: '₹14/kg', status: 'Completed' }
    ];

    records.forEach(record => {
      const listItem = document.createElement('li');
      listItem.innerText = `Contract with ${record.buyer} - ${record.price} - ${record.status}`;
      recordsList.appendChild(listItem);
    });
  } else {
    console.error("Element with id 'records-list' not found.");
  }
}

// Price Data
// Initialize data for price trends with initial dummy data
const priceData = {
  labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6'],
  datasets: [{
    label: 'Crop Price (₹)',
    data: [2200, 2300, 2150, 2250, 2350, 2400], // Initial price points
    borderColor: 'rgba(75, 192, 192, 1)',
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderWidth: 2,
    tension: 0.2
  }]
};

// Create the price trends chart
const ctx = document.getElementById('priceChart').getContext('2d');
const priceChart = new Chart(ctx, {
  type: 'line',
  data: priceData,
  options: {
    responsive: true,
    plugins: {
      legend: { display: true, position: 'top' }
    },
    scales: {
      y: {
        beginAtZero: false,
        suggestedMin: 2000, // Minimum range for better visualization
        suggestedMax: 2500 // Maximum range for better visualization
      }
    }
  }
});

// Function to add a daily price update
function updateDailyPrice() {
  // Generate a random price between 2100 and 2400
  const newPrice = Math.floor(Math.random() * (2400 - 2100 + 1)) + 2100;

  // Add the new price to the dataset and a new label for the day
  const nextDayLabel = `Day ${priceChart.data.labels.length + 1}`;
  priceChart.data.datasets[0].data.push(newPrice);
  priceChart.data.labels.push(nextDayLabel);

  // Update the live price display and chart
  document.getElementById('live-price').innerText = `Current Price: ₹${newPrice}/kg`;
  priceChart.update();
}

// Simulate daily price update at 24-hour intervals (86400000 milliseconds)
setInterval(updateDailyPrice, 86400000); // 24 hours in milliseconds

// Initial call to show today's price on load
updateDailyPrice();

