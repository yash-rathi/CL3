import java.util.*;
import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.*;

public class Cloudsim {

	private static List<Cloudlet> cloudletList;
	private static List<Vm> vmList;
	
	public static void main(String[] args) {
		Log.printLine("Starting Cloudsim...");
		
		try {
			CloudSim.init(0, Calendar.getInstance(), false);
			
			List<Host> hostList = new ArrayList<Host>();
			List<Pe> peList = new ArrayList<Pe>();
			List<Storage> storageList = new ArrayList<Storage>();
			peList.add(new Pe(0, new PeProvisionerSimple(1000)));
			hostList.add(new Host(0, new RamProvisionerSimple(2048), new BwProvisionerSimple(10000), 1000000, peList, new VmSchedulerTimeShared(peList)));
			DatacenterCharacteristics characteristics = new DatacenterCharacteristics("x86", "Linux", "Xen", hostList, 10.0, 3.0, 0.05, 0.001, 0);
			Datacenter datacenter  = new Datacenter("Datacenter0", characteristics, new VmAllocationPolicySimple(hostList), storageList, 0);
			
			DatacenterBroker broker = new DatacenterBroker("Broker");
			int brokerId = broker.getId();
			
			vmList = new ArrayList<Vm>();
			vmList.add(new Vm(0, brokerId, 1000, 1, 512, 1000, 10000, "Xen", new CloudletSchedulerTimeShared()));
			broker.submitVmList(vmList);
			
			cloudletList = new ArrayList<Cloudlet>();
			UtilizationModel utilizationModel = new UtilizationModelFull();
			Cloudlet cloudlet = new Cloudlet(0, 40000, 1, 300, 300, utilizationModel, utilizationModel, utilizationModel);
			cloudlet.setUserId(brokerId);
			cloudlet.setVmId(0);
			cloudletList.add(cloudlet);
			broker.submitCloudletList(cloudletList);
			
			CloudSim.startSimulation();
			CloudSim.stopSimulation();
			
			List<Cloudlet> list = broker.getCloudletReceivedList();
			Cloudlet cl;
			String indent = "		";
			Log.printLine("Cloudlet Id" + indent + "Status" + indent + "Datacenter Id" + indent + "Vm Id" + indent + "Time" + indent + "Start Time" + indent + "Finish Time");
			for(int i = 0; i < list.size(); i ++) {
				cl = list.get(i);
				Log.print(cl.getCloudletId() + indent);
				if(cl.getCloudletStatus() == Cloudlet.SUCCESS) {
					Log.print("SUCCESS");
				}
				Log.printLine(indent + cl.getResourceId() + indent + cl.getVmId() + indent + cl.getActualCPUTime() + indent + cl.getExecStartTime() + indent + cl.getFinishTime());
				Log.printLine("Response Time = " + (cl.getFinishTime() - cl.getSubmissionTime()));
				Log.printLine("Execution Time = " + (cl.getFinishTime() - cl.getExecStartTime()));
			}
			datacenter.printDebts();
			Log.printLine("Cloudsim finished!");
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
}
