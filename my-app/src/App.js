import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './styles.css';


function ProfileScreen() {
  return (
    <div>
      <h2>Profile Screen</h2>
    </div>
  );
}

function ExerciseGeneratorScreen() {
  return (
    <div>
      <h2>Exercise Generator Screen</h2>
    </div>
  );
}

function ProblemSolverScreen() {
  return (
    <div>
      <h2>Problem Solver Screen</h2>
    </div>
  );
}

function ScoreScreen() {
  return (
    <div>
      <h2>Score Screen</h2>
    </div>
  );
}

function CoursesScreen() {
  return (
    <div>
      <h2>Courses Screen</h2>
    </div>
  );
}


function MyTabs() {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Profile</Link>
          </li>
          <li>
            <Link to="/exercise-generator">Exercise Generator</Link>
          </li>
          <li>
            <Link to="/problem-solver">Problem Solver</Link>
          </li>
          <li>
            <Link to="/score">Score</Link>
          </li>
          <li>
            <Link to="/courses">Courses</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/exercise-generator" element={<ExerciseGeneratorScreen />} />
        <Route path="/problem-solver" element={<ProblemSolverScreen />} />
        <Route path="/score" element={<ScoreScreen />} />
        <Route path="/courses" element={<CoursesScreen />} />
        <Route path="/" element={<ProfileScreen />} />
      </Routes>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <MyTabs />
    </Router>
  );
}
