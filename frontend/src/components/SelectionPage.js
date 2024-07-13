import React, { useState, useEffect } from 'react';
import axios from 'axios';

// SignPage component with a form to collect user details
const SignPage = () => {
  // State variables to store dropdown options and form data
  const [counties, setCounties] = useState([]);
  const [constituencies, setConstituencies] = useState([]);
  const [wards, setWards] = useState([]);
  const [pollingStations, setPollingStations] = useState([]);

  const [form, setForm] = useState({
    name: '',
    id_or_passport_number: '',
    county: '',
    constituency: '',
    ward: '',
    polling_station: '',
    mobile_number: '',
    signature: ''
  });

  // Fetch counties on component mount
  useEffect(() => {
    axios.get('/api/counties/')
      .then(response => {
        setCounties(response.data);
        console.log(response.data)
      })
      .catch(error => {
        console.error('Error fetching counties:', error);
      });
  }, []);

// Handle change for county dropdown
const handleCountyChange = (e) => {
  setForm({ ...form, county: e.target.value });
  axios.get(`/api/counties/${e.target.value}/constituencies`)
    .then(response => setConstituencies(response.data))
    .catch(error => {
      console.error('Error fetching constituencies:', error);
      // Handle error, e.g., display an error message to the user
    });
};

// Handle change for constituency dropdown
const handleConstituencyChange = (e) => {
  setForm({ ...form, constituency: e.target.value });
  axios.get(`/api/constituencies/${e.target.value}/wards`)
    .then(response => setWards(response.data))
    .catch(error => {
      console.error('Error fetching wards:', error);
      // Handle error, e.g., display an error message to the user
    });
};

// Handle change for ward dropdown
const handleWardChange = (e) => {
  setForm({ ...form, ward: e.target.value });
  axios.get(`/api/wards/${e.target.value}/polling_stations`)
    .then(response => setPollingStations(response.data))
    .catch(error => {
      console.error('Error fetching polling stations:', error);
      // Handle error, e.g., display an error message to the user
    });
};


  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/entries', form)
      .then(response => {
        console.log('Form submitted successfully');
      })
      .catch(error => {
        if (error.response && error.response.status === 400) {
          console.error('Bad request error:', error)
        } else if (error.response && error.response.status === 500) {
          console.error('Server error:', error)
        } else {
          console.error('Other error:', error)
        }
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Input for Name */}
      <input
        type="text"
        placeholder="Name"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />
      {/* Input for ID/Passport Number */}
      <input
        type="text"
        placeholder="ID/Passport Number"
        value={form.id_or_passport_number}
        onChange={(e) => setForm({ ...form, id_or_passport_number: e.target.value })}
      />
      {/* Dropdown for County */}
      <select value={form.county} onChange={handleCountyChange}>
        <option value="">Select County</option>
        {counties.map(county => <option key={county.id} value={county.id}>{county.name}</option>)}
      </select>
      {/* Dropdown for Constituency */}
      <select value={form.constituency} onChange={handleConstituencyChange}>
        <option value="">Select Constituency</option>
        {constituencies.map(constituency => <option key={constituency.id} value={constituency.id}>{constituency.name}</option>)}
      </select>
      {/* Dropdown for Ward */}
      <select value={form.ward} onChange={handleWardChange}>
        <option value="">Select Ward</option>
        {wards.map(ward => <option key={ward.id} value={ward.id}>{ward.name}</option>)}
      </select>
      {/* Dropdown for Polling Station */}
      <select value={form.polling_station} onChange={(e) => setForm({ ...form, polling_station: e.target.value })}>
        <option value="">Select Polling Station</option>
        {pollingStations.map(station => <option key={station.id} value={station.id}>{station.name}</option>)}
      </select>
      {/* Input for Mobile Number */}
      <input
        type="text"
        placeholder="Mobile Number"
        value={form.mobile_number}
        onChange={(e) => setForm({ ...form, mobile_number: e.target.value })}
      />
      {/* Input for Signature */}
      <input
        type="text"
        placeholder="Signature"
        value={form.signature}
        onChange={(e) => setForm({ ...form, signature: e.target.value })}
      />
      {/* Submit Button */}
      <button type="submit">Submit</button>
    </form>
  );
};

export default SignPage;