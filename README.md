# Mirae2


### 가상환경 만들기
- python -m venv "가상환경이름"

### 가상환경 실행
- "가상환경이름'\Scripts\activate

### 필요 패키지 설치
- pip install -r requirements.txt


### javascript 임시

```javascript
import React, { useState } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

function ObservationForm() {
  const [obsCode, setObsCode] = useState('');
  const [date, setDate] = useState(new Date());
  const [result, setResult] = useState(null);

  const handleDateChange = (selectedDate) => {
    setDate(selectedDate);
  };

  const fetchData = () => {
    axios
      .get(`/api/observation/?ObsCode=${obsCode}&Date=${date}`)
      .then((response) => {
        setResult(response.data);
      })
      .catch((error) => {
        console.error("API request failed:", error);
      });
  };

  return (
    <div>
      <h1>Get Observation Data</h1>
      <label htmlFor="obs-code">Observation Code:</label>
      <input
        type="text"
        id="obs-code"
        value={obsCode}
        onChange={(e) => setObsCode(e.target.value)}
      />
      <br />
      <label>Date:</label>
      <DatePicker selected={date} onChange={handleDateChange} />
      <br />
      <button onClick={fetchData}>Get Data</button>
      <div id="result">
        {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
      </div>
    </div>
  );
}

export default ObservationForm;



```
