import React from 'react'
import Container from './Container'

const Footer = () => {
  return (
    <footer className="border-t mt-20 py-8">
      <Container>
        <p className="text-center text-gray-500">
          © {new Date().getFullYear()} InterviewAI. All rights reserved.
        </p>
      </Container>
    </footer>
  )
}

export default Footer