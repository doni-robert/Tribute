import React, { useEffect, useState } from 'react';
import axios from 'axios';

// ViewPage component to display entries and download as PDF
const ViewPage = () => {
  const [entries, setEntries] = useState([]);

  // Fetch entries on component mount
  useEffect(() => {
    axios.get('/api/entries').then(response => setEntries(response.data));
  }, []);

  // Function to download entries as PDF
  const downloadPDF = () => {
    axios.get('/api/entries/pdf', { responseType: 'blob' }).then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'signatures.pdf');
      document.body.appendChild(link);
      link.click();
    });
  };

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>ID/Passport Number</th>
            <th>County</th>
            <th>Constituency</th>
            <th>Ward</th>
            <th>Polling Station</th>
            <th>Mobile Number</th>
            <th>Signature</th>
          </tr>
        </thead>
        <tbody>
          {entries.map(entry => (
            <tr key={entry.id}>
              <td>{entry.name}</td>
              <td>{entry.id_or_passport_number}</td>
              <td>{entry.county}</td>
              <td>{entry.constituency}</td>
              <td>{entry.ward}</td>
              <td>{entry.polling_station}</td>
              <td>{entry.mobile_number}</td>
              <td>{entry.signature}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {/* Button to download the table data as a PDF */}
      <button onClick={downloadPDF}>Download as PDF</button>
    </div>
  );
};

export default ViewPage;