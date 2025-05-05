import { useState } from 'react';

export default function App() {
  const [city, setCity] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('http://127.0.0.1:8000/insights', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city })
      });
      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>SmartCity Insights</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          required
        />
        <button type="submit">Get Insights</button>
      </form>
      {loading && <p>Loading...</p>}
      {error && <p className="error">Error: {error}</p>}
      {result && (
        <div className="result">
          <h2>Results for {result.city}</h2>
          <p><strong>Weather:</strong> {result.weather}</p>
          <p><strong>Summary:</strong> {result.summary}</p>
        </div>
      )}
    </div>
  );
}