import RecatMediaRecorder, { ReactMediaRecorder } from 'react-media-recorder'
import RecordIcon from './RecordIcon'
type Props = {
    handleStop : any
}

function RecordMessage({handleStop}: Props) {
  return (
    <ReactMediaRecorder

    audio
    onStop={handleStop}
    render={({ status, startRecording, stopRecording}: any) => 
    <div className='mt-2'>
        <button onMouseDown={startRecording} onMouseUp = {stopRecording} className='bg-white p-4 rounded-full'><RecordIcon ClassText={status == "recording" ? "animate-pulse text-red-500" : "text-sky-500"}/></button>
        <p className='text-white mt-2 font-light'>{status}</p>
    </div> }
    />
  )
}

export default RecordMessage