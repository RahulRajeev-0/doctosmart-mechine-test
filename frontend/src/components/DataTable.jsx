import * as React from 'react';
import  {useEffect, useState} from 'react'
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'first_name', headerName: 'First name', width: 130 },
  { field: 'last_name', headerName: 'Last name', width: 130 },
  { field: 'address', headerName: 'Address', width: 200 },
  {
    field: 'date_of_birth',
    headerName: 'Date of Birth',
    
    width: 160,
  },
  {
    field: 'phone_number',
    headerName: 'Phone number',
   
    width: 150,
  },
  {
    field: 'email',
    headerName: 'Email',
    type: 'email',
    width: 150,
  },
  {
    field: 'Action',
    headerName: 'Action',
    type: 'number',
    width: 150,
  },
  
];



export default function DataTable() {
  const [rows, setRows] = useState([])
  const baseURL = 'http://localhost:8000'
  
  const fatchPatients = async()=> {
   
      const res = await axios.get(baseURL+`/patients/`)
      console.log(res.data);
      setRows(res.data)

  }
  useEffect(()=>{
    fatchPatients()
  },[])

  return (
    <div style={{ height: 400, width: '90%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 5 },
          },
        }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
    </div>
  );
}
