import {Outlet} from 'react-router-dom' 
import Navbar from './Navbar'
import Footer from './Footer'

const MainLayout = () => {
  return (
    <div className='min-h-screen  bg-[#080B12] text-[#F5F7FA] flex flex-col'>
        <Navbar />
        <main className="flex-1">
            <Outlet />
        </main>
        <Footer />
    </div>
  )
}


export default MainLayout
