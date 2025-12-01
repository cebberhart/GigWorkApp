// GigWork Frontend - Complete JavaScript
// Connects HTML to Flask Backend

const API_URL = 'http://localhost:5000';
let authToken = localStorage.getItem('token');
let currentUser = JSON.parse(localStorage.getItem('user')) || null;

// AUTHENTICATION

async function loginUser(email, password) {
  try {
    const response = await fetch(`${API_URL}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok) {
      authToken = data.token;
      currentUser = data.user;
      
      localStorage.setItem('token', authToken);
      localStorage.setItem('user', JSON.stringify(currentUser));
      
      showPopup('Login successful!');
      
      // Redirect based on role
      if (currentUser.role === 'client') {
        setTimeout(() => window.location.href = '/dash', 1000);
      } else {
        setTimeout(() => window.location.href = '/worker-dash', 1000);
      }
      return true;
    } else {
      showPopup(`Login failed: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

async function registerUser(name, email, password, role) {
  try {
    const response = await fetch(`${API_URL}/auth/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, password, role })
    });

    const data = await response.json();

    if (response.ok) {
      authToken = data.token;
      currentUser = data.user;
      
      localStorage.setItem('token', authToken);
      localStorage.setItem('user', JSON.stringify(currentUser));
      
      showPopup('Registration successful!');
      
      // Redirect based on role
      if (currentUser.role === 'client') {
        setTimeout(() => window.location.href = '/dash', 1000);
      } else {
        setTimeout(() => window.location.href = '/worker-dash', 1000);
      }
      return true;
    } else {
      showPopup(`Registration failed: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

// GIGS

async function fetchGigs(page = 1, location = null, paymentMin = null) {
  try {
    let url = `${API_URL}/gigs?page=${page}`;
    
    if (location) url += `&location=${location}`;
    if (paymentMin) url += `&payment_min=${paymentMin}`;

    const response = await fetch(url);
    const data = await response.json();

    if (response.ok) {
      return data.gigs;
    } else {
      showPopup(`Error fetching gigs: ${data.error}`);
      return [];
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return [];
  }
}

function displayGigsInList(gigs, containerId = 'gig-list') {
  const container = document.getElementById(containerId) || document.querySelector('.gig-list');
  
  if (!container) return;
  
  container.innerHTML = '';

  if (gigs.length === 0) {
    container.innerHTML = '<p style="text-align:center;">No gigs available</p>';
    return;
  }

  gigs.forEach(gig => {
    const gigElement = document.createElement('div');
    gigElement.className = 'gig';
    gigElement.innerHTML = `
      <h4>${gig.title}</h4>
      <small>${gig.location} • Status: ${gig.status}</small>
      <span>$${gig.payment}</span>
      <button onclick="applyForGig(${gig.id})" class="btn" style="margin-top: 10px; width: 100%; padding: 8px;">Apply Now</button>
    `;
    container.appendChild(gigElement);
  });
}

async function loadAvailableGigs() {
  const gigs = await fetchGigs();
  displayGigsInList(gigs);
}

// GIGS - CREATE (for Clients)

async function createGig(title, description, location, payment, category) {
  if (!authToken) {
    showPopup('Please login first!');
    return false;
  }

  if (currentUser.role !== 'client') {
    showPopup('Only clients can create gigs!');
    return false;
  }

  try {
    const response = await fetch(`${API_URL}/gigs`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
      },
      body: JSON.stringify({
        title,
        description,
        location,
        payment: parseFloat(payment),
        category
      })
    });

    const data = await response.json();

    if (response.ok) {
      showPopup('Gig created successfully! 🎉');
      return data;
    } else {
      showPopup(`Error: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

// APPLICATIONS

async function applyForGig(gigId) {
  if (!authToken) {
    showPopup('Please login first!');
    window.location.href = '/register';
    return;
  }

  if (currentUser.role !== 'worker') {
    showPopup('Only workers can apply for gigs!');
    return;
  }

  try {
    const response = await fetch(`${API_URL}/applications`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
      },
      body: JSON.stringify({
        gig_id: parseInt(gigId),
        message: 'I am interested in this gig!'
      })
    });

    const data = await response.json();

    if (response.ok) {
      showPopup('Application submitted! 🎉');
    } else {
      showPopup(`Error: ${data.error}`);
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
  }
}

async function getMyApplications() {
  if (!authToken) {
    return [];
  }

  try {
    const response = await fetch(`${API_URL}/applications`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      return data.applications;
    } else {
      return [];
    }
  } catch (error) {
    console.error('Error fetching applications:', error);
    return [];
  }
}

function displayMyApplications(applications) {
  const container = document.querySelector('.gig-list');
  
  if (!container) return;
  
  container.innerHTML = '';

  if (applications.length === 0) {
    container.innerHTML = '<p style="text-align:center;">No applications yet</p>';
    return;
  }

  applications.forEach(app => {
    const appElement = document.createElement('div');
    appElement.className = 'gig';
    appElement.innerHTML = `
      <h4>Gig ID: ${app.gig_id}</h4>
      <small>Status: ${app.status}</small>
      <p>Applied: ${app.created_at}</p>
    `;
    container.appendChild(appElement);
  });
}

// APPLICATIONS - CLIENT VIEW

async function getClientApplications() {
  if (!authToken) {
    return [];
  }

  if (currentUser.role !== 'client') {
    console.log('Only clients can view applications to their gigs');
    return [];
  }

  try {
    const response = await fetch(`${API_URL}/applications`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      return data.applications;
    } else {
      console.error('Error:', data.error);
      return [];
    }
  } catch (error) {
    console.error('Error fetching client applications:', error);
    return [];
  }
}

function displayClientApplications(applications) {
  const container = document.querySelector('.gig-list');
  
  if (!container) return;
  
  container.innerHTML = '';

  if (applications.length === 0) {
    container.innerHTML = '<p style="text-align:center;">No applications received yet</p>';
    return;
  }

  applications.forEach(app => {
    const appElement = document.createElement('div');
    appElement.className = 'gig';
    appElement.innerHTML = `
      <h4>${app.worker_name || 'Worker'}</h4>
      <small>Gig: ${app.gig_title || `ID ${app.gig_id}`}</small>
      <p>Status: <strong>${app.status}</strong></p>
      <p>Message: ${app.message || 'No message'}</p>
      <p>Applied: ${app.created_at}</p>
      ${app.status === 'pending' ? `
        <button onclick="acceptApplication(${app.id})" class="btn" style="width: 100%; margin-top: 10px;">
          Accept Application
        </button>
      ` : ''}
    `;
    container.appendChild(appElement);
  });
}

// APPLICATIONS - ACCEPT

async function acceptApplication(applicationId) {
  if (!authToken) {
    showPopup('Please login first!');
    return false;
  }

  if (currentUser.role !== 'client') {
    showPopup('Only clients can accept applications!');
    return false;
  }

  try {
    const response = await fetch(`${API_URL}/applications/${applicationId}/accept`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      showPopup('Application accepted! 🎉');
      // Refresh the applications list
      const apps = await getClientApplications();
      displayClientApplications(apps);
      return true;
    } else {
      showPopup(`Error: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

// NOTIFICATIONS

async function getNotifications() {
  if (!authToken) {
    return [];
  }

  try {
    const response = await fetch(`${API_URL}/notifications`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      return data.notifications;
    } else {
      return [];
    }
  } catch (error) {
    console.error('Error fetching notifications:', error);
    return [];
  }
}

// NOTIFICATIONS - UNREAD ONLY

async function getUnreadNotifications() {
  if (!authToken) {
    return [];
  }

  try {
    const response = await fetch(`${API_URL}/notifications/unread`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      return data.notifications;
    } else {
      return [];
    }
  } catch (error) {
    console.error('Error fetching unread notifications:', error);
    return [];
  }
}

async function getUnreadNotificationCount() {
  const unreadNotifs = await getUnreadNotifications();
  return unreadNotifs.length;
}

// NOTIFICATIONS - MARK AS READ

async function markNotificationAsRead(notificationId) {
  if (!authToken) {
    return false;
  }

  try {
    const response = await fetch(`${API_URL}/notifications/${notificationId}/read`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      return true;
    } else {
      console.error('Error marking notification as read:', data.error);
      return false;
    }
  } catch (error) {
    console.error('Error:', error);
    return false;
  }
}

// NOTIFICATIONS - DELETE

async function deleteNotification(notificationId) {
  if (!authToken) {
    return false;
  }

  try {
    const response = await fetch(`${API_URL}/notifications/${notificationId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authToken}`
      }
    });

    const data = await response.json();

    if (response.ok) {
      showPopup('Notification deleted');
      return true;
    } else {
      showPopup(`Error: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

// NOTIFICATIONS - DISPLAY WITH ACTIONS

function displayNotifications(notifications) {
  const container = document.querySelector('.notifications-container');
  
  if (!container) return;
  
  container.innerHTML = '';

  if (notifications.length === 0) {
    container.innerHTML = '<p style="text-align:center;">No notifications</p>';
    return;
  }

  notifications.forEach(notif => {
    const notifElement = document.createElement('div');
    notifElement.className = `notification ${notif.read ? 'read' : 'unread'}`;
    notifElement.style.cssText = `
      background: ${notif.read ? '#f5f5f5' : '#e8f4ff'};
      padding: 15px;
      margin-bottom: 10px;
      border-radius: 8px;
      border-left: 4px solid ${notif.read ? '#ccc' : '#4a4aff'};
    `;
    
    notifElement.innerHTML = `
      <p><strong>${notif.message}</strong></p>
      <small>${notif.created_at}</small>
      <div style="margin-top: 10px;">
        ${!notif.read ? `
          <button onclick="markNotificationAsRead(${notif.id})" class="btn" style="padding: 5px 10px; font-size: 0.9rem;">
            Mark as Read
          </button>
        ` : ''}
        <button onclick="deleteNotification(${notif.id})" class="btn" style="padding: 5px 10px; font-size: 0.9rem; background: #ff4444;">
          Delete
        </button>
      </div>
    `;
    container.appendChild(notifElement);
  });
}

// HELPER: Update notification badge count
async function updateNotificationBadge() {
  const count = await getUnreadNotificationCount();
  const badge = document.getElementById('notification-badge');
  
  if (badge) {
    if (count > 0) {
      badge.textContent = count;
      badge.style.display = 'inline-block';
    } else {
      badge.style.display = 'none';
    }
  }
}

// REVIEWS

async function leaveReview(gigId, rating, text) {
  if (!authToken) {
    showPopup('Please login first!');
    return;
  }

  try {
    const response = await fetch(`${API_URL}/reviews`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
      },
      body: JSON.stringify({
        gig_id: parseInt(gigId),
        rating: parseInt(rating),
        text: text
      })
    });

    const data = await response.json();

    if (response.ok) {
      showPopup('Review submitted!');
      return true;
    } else {
      showPopup(`Error: ${data.error}`);
      return false;
    }
  } catch (error) {
    showPopup(`Error: ${error.message}`);
    return false;
  }
}

// UTILITY FUNCTIONS

function showPopup(message) {
  // Create popup if it doesn't exist
  let popup = document.getElementById('popup');
  if (!popup) {
    popup = document.createElement('div');
    popup.id = 'popup';
    popup.style.cssText = `
      position: fixed;
      bottom: -100px;
      left: 50%;
      transform: translateX(-50%);
      background: #4a4aff;
      color: white;
      padding: 15px 25px;
      border-radius: 10px;
      font-size: 1.1rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      transition: bottom 0.4s ease;
      z-index: 1000;
    `;
    document.body.appendChild(popup);
  }

  popup.textContent = message;
  popup.style.bottom = '30px';
  
  setTimeout(() => {
    popup.style.bottom = '-100px';
  }, 3000);
}

function logout() {
  authToken = null;
  currentUser = null;
  localStorage.removeItem('token');
  localStorage.removeItem('user');
  showPopup('Logged out successfully!');
  setTimeout(() => window.location.href = '/login', 1000);
}

function isLoggedIn() {
  return authToken !== null && authToken !== undefined;
}

function logout() {
  localStorage.clear();
  sessionStorage.clear();
  window.location.href = "/login";
}


function getCurrentUser() {
  return currentUser;
}

// INITIALIZATION

document.addEventListener('DOMContentLoaded', () => {
  // Check if user is logged in
  if (isLoggedIn()) {
    console.log(`Logged in as: ${currentUser.name} (${currentUser.role})`);
  }

  // Auto-refresh gigs every 30 seconds on available gigs page
  if (window.location.pathname.includes('GWAvailble.html')) {
    loadAvailableGigs();
    setInterval(loadAvailableGigs, 30000);
  }
});