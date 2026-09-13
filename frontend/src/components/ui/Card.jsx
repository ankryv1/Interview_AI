
const Card = ({children, className="", onClick}) => {
  return (
    <div 
    onClick={onClick}
    className={`bg-[#121826] rounded-xl shadow-md 
            border border-gray-200 p-6 transition 
            hover:shadow-lg ${className}`}>
        {children}
    </div>
  )
}

export default Card
