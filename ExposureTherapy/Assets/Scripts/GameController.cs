using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameController : MonoBehaviour
{
    public GameObject player;
    public Transform level2Spawn;
    public Transform level3Spawn;
    public Transform level4Spawn;

    Dictionary<int, Transform> spawns;

    int currentLevel = 1;

    bool timerRunning = false;
    float targetTime = 20f;

    public Transform farPlaneSpawn;
    public GameObject farPlanePrefab;

    public Canvas proceedGate202;

    public GameObject airport;

    public GameObject plane;

    public GameObject[] level4RemoveList;

    public Canvas ending;

    private void Awake()
    {
        spawns = new Dictionary<int, Transform>();
        spawns.Add(2, level2Spawn);
        spawns.Add(3, level3Spawn);
        spawns.Add(4, level4Spawn);
        proceedGate202.enabled = false;
        plane.SetActive(false);
        ending.enabled = false;
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (timerRunning)
        {
            targetTime -= Time.deltaTime;

            if (targetTime <= 0.0f)
            {
                timerEnded();
            }
        }

        if (currentLevel == 2)
        {
            if (!proceedGate202.enabled)
            {
                proceedGate202.enabled = true;
            }
            if (!timerRunning)
            {
                startTimer(20f);
            }
        }

        if (currentLevel == 4)
        {
            if (Input.GetKeyDown(KeyCode.Return))
            {
                print("Exiting application");
                Application.Quit();
                UnityEditor.EditorApplication.isPlaying = false;
            }
        }
    }

    void SpawnFarPlane()
    {
        Instantiate(farPlanePrefab, farPlaneSpawn.position, Quaternion.Euler(15f, 90f, 0f));
    }

    public void startTimer(float givenTime)
    {
        targetTime = givenTime;
        timerRunning = true;
        SpawnFarPlane();
    }

    void timerEnded()
    {
        timerRunning = false;
    }

    public int GetCurrentLevel()
    {
        return currentLevel;
    }

    public void NextLevel()
    {
        print("Going to next level");
        currentLevel++;
        player.transform.position = spawns[currentLevel].position;
        if (currentLevel == 3)
        {
            Destroy(airport);
            plane.SetActive(true);
        }
        if (currentLevel == 4)
        {
            player.GetComponent<PlayerMovement>().DisableMovement();
            foreach (var elem in level4RemoveList)
            {
                Destroy(elem);
            }
            ending.enabled = true;
        }
    }
}
