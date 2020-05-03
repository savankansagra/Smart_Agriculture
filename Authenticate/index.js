// Import stylesheets
import './style.css';
// Firebase App (the core Firebase SDK) is always required and must be listed first
import * as firebase from "firebase/app";

// Add the Firebase products that you want to use
import "firebase/auth";
import "firebase/firestore";

import * as firebaseui from 'firebaseui';

// Document elements
const startRsvpButton = document.getElementById('startRsvp');
const guestbookContainer = document.getElementById('guestbook-container');

const form = document.getElementById('leave-message');
const input = document.getElementById('message');
const guestbook = document.getElementById('guestbook');
const numberAttending = document.getElementById('number-attending');
const rsvpYes = document.getElementById('rsvp-yes');
const rsvpNo = document.getElementById('rsvp-no');

var rsvpListener = null;
var guestbookListener = null;

// Add Firebase project configuration object here
// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyBF0BDer4ZjffMXDX8Uqm6bJKj9sGo3T94",
  authDomain: "learnex1.firebaseapp.com",
  databaseURL: "https://learnex1.firebaseio.com",
  projectId: "learnex1",
  storageBucket: "learnex1.appspot.com",
  messagingSenderId: "778812217996",
  appId: "1:778812217996:web:73253cbbeb0ac9b4cf39a9"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// FirebaseUI config
const uiConfig = {
  credentialHelper: firebaseui.auth.CredentialHelper.NONE,
  signInOptions: [
    // Email / Password Provider.
    firebase.auth.EmailAuthProvider.PROVIDER_ID
  ],
  callbacks: {
    signInSuccessWithAuthResult: function(authResult, redirectUrl){
      // Handle sign-in.
      // Return false to avoid redirect.
      return false;
    }
  }
};

// const ui = new firebaseui.auth.AuthUI(firebase.auth());
